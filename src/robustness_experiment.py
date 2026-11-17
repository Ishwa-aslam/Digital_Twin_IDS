
import numpy as np
import pandas as pd

from sklearn.model_selection import GroupShuffleSplit
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

df = pd.read_csv("data/combined_dataset.csv")

df["valve_status"] = df["valve_status"].map({
    "OPEN": 1,
    "CLOSED": 0
})

features = ["water_level", "flow_rate", "valve_status"]
X = df[features]
y = df["status"].map({"Normal": 0, "Anomaly": 1})

splitter = GroupShuffleSplit(
    n_splits=1,
    test_size=0.20,
    random_state=42
)

train_idx, test_idx = next(
    splitter.split(X, y, groups=df["time"])
)

X_train = X.iloc[train_idx].copy()
X_test = X.iloc[test_idx].copy()
y_train = y.iloc[train_idx].copy()
y_test = y.iloc[test_idx].copy()

def evaluate(name, model, test_data):
    predictions = model.predict(test_data)

    return {
        "Experiment": name,
        "Accuracy": accuracy_score(y_test, predictions),
        "Precision": precision_score(
            y_test, predictions, zero_division=0
        ),
        "Recall": recall_score(
            y_test, predictions, zero_division=0
        ),
        "F1 Score": f1_score(
            y_test, predictions, zero_division=0
        )
    }

results = []

# 1. Normal test data
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
model.fit(X_train, y_train)

results.append(
    evaluate("Clean Test Data", model, X_test)
)

# 2. Noisy sensor readings
rng = np.random.default_rng(42)
noisy_test = X_test.copy()

noisy_test["water_level"] += rng.normal(
    0, 5, size=len(noisy_test)
)
noisy_test["flow_rate"] += rng.normal(
    0, 2, size=len(noisy_test)
)

noisy_test["water_level"] = noisy_test[
    "water_level"
].clip(0, 100)

noisy_test["flow_rate"] = noisy_test[
    "flow_rate"
].clip(lower=0)

results.append(
    evaluate("Noisy Test Data", model, noisy_test)
)

# 3. Missing sensor readings
missing_test = X_test.copy()

for column in ["water_level", "flow_rate"]:
    missing_indices = rng.choice(
        missing_test.index,
        size=max(1, int(len(missing_test) * 0.10)),
        replace=False
    )
    missing_test.loc[missing_indices, column] = np.nan

training_medians = X_train.median()
missing_test = missing_test.fillna(training_medians)

results.append(
    evaluate("Missing Values Test", model, missing_test)
)

# 4. Imbalanced training data
normal_data = X_train[y_train == 0]
anomaly_data = X_train[y_train == 1]

reduced_anomalies = anomaly_data.sample(
    n=max(1, int(len(normal_data) * 0.25)),
    random_state=42
)

imbalanced_X = pd.concat([
    normal_data,
    reduced_anomalies
])

imbalanced_y = pd.concat([
    y_train.loc[normal_data.index],
    y_train.loc[reduced_anomalies.index]
])

imbalanced_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

imbalanced_model.fit(imbalanced_X, imbalanced_y)

results.append(
    evaluate("Imbalanced Training Data", imbalanced_model, X_test)
)

results_df = pd.DataFrame(results)

print("\nROBUSTNESS EXPERIMENT RESULTS")
print(results_df.to_string(index=False))

results_df.to_csv(
    "results/robustness_experiment.csv",
    index=False
)

print("\nRobustness experiment completed!")
print("Results saved successfully!")
