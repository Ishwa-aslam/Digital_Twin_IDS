
import time
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

# 1. Load dataset
df = pd.read_csv("data/combined_dataset.csv")

df["anomaly_type"] = df["anomaly_type"].fillna("None")

# 2. Prepare features and target
X = df[["water_level", "flow_rate", "valve_status"]].copy()

X["valve_status"] = X["valve_status"].map({
    "OPEN": 1,
    "CLOSED": 0
})

y = df["status"].map({
    "Normal": 0,
    "Anomaly": 1
})

# 3. Split dataset
from sklearn.model_selection import GroupShuffleSplit

splitter = GroupShuffleSplit(
    n_splits=1,
    test_size=0.20,
    random_state=42
)

train_idx, test_idx = next(
    splitter.split(X, y, groups=df["time"])
)

X_train = X.iloc[train_idx]
X_test = X.iloc[test_idx]

y_train = y.iloc[train_idx]
y_test = y.iloc[test_idx]

# 4. Scale features
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 5. Define ML models
models = {
    "Logistic Regression": LogisticRegression(random_state=42),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )
}

results = []

# 6. Train and evaluate models
for name, model in models.items():

    start_time = time.perf_counter()

    model.fit(X_train_scaled, y_train)

    training_time = time.perf_counter() - start_time

    predictions = model.predict(X_test_scaled)

    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(y_test, predictions, zero_division=0)
    recall = recall_score(y_test, predictions, zero_division=0)
    f1 = f1_score(y_test, predictions, zero_division=0)

    results.append({
        "Model": name,
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1 Score": f1,
        "Training Time (seconds)": training_time
    })

    print("\n" + "=" * 45)
    print(name)
    print("=" * 45)

    print(classification_report(
        y_test,
        predictions,
        target_names=["Normal", "Anomaly"],
        zero_division=0
    ))

    # Save confusion matrix
    cm = confusion_matrix(y_test, predictions)

    display = ConfusionMatrixDisplay(
        confusion_matrix=cm,
        display_labels=["Normal", "Anomaly"]
    )

    display.plot()
    plt.title(name + " - Confusion Matrix")
    plt.savefig(
        "figures/" + name.lower().replace(" ", "_") + "_cm.png"
    )
    plt.close()

# 7. Compare models
results_df = pd.DataFrame(results)

print("\n\nMODEL COMPARISON")
print(results_df.to_string(index=False))

results_df.to_csv("results/model_comparison.csv", index=False)

print("\nModel results saved successfully!")
