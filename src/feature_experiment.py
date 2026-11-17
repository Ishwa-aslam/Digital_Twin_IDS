
import time
import pandas as pd
from sklearn.model_selection import GroupShuffleSplit
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Load dataset
df = pd.read_csv("data/combined_dataset.csv")

# Encode categorical values
df["valve_status"] = df["valve_status"].map({
    "OPEN": 1,
    "CLOSED": 0
})

y = df["status"].map({
    "Normal": 0,
    "Anomaly": 1
})

# Keep related records in the same split
splitter = GroupShuffleSplit(
    n_splits=1,
    test_size=0.20,
    random_state=42
)

train_idx, test_idx = next(
    splitter.split(df, y, groups=df["time"])
)

# Define feature groups
feature_groups = {
    "Process Features": ["water_level", "flow_rate"],
    "Control Feature": ["valve_status"],
    "All Features": ["water_level", "flow_rate", "valve_status"]
}

results = []

# Run experiments
for name, features in feature_groups.items():

    X = df[features]

    X_train = X.iloc[train_idx]
    X_test = X.iloc[test_idx]

    y_train = y.iloc[train_idx]
    y_test = y.iloc[test_idx]

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    start = time.perf_counter()

    model.fit(X_train, y_train)

    training_time = time.perf_counter() - start

    # Measure average prediction latency
    start = time.perf_counter()

    for _ in range(100):
        model.predict(X_test)

    total_prediction_time = time.perf_counter() - start

    avg_latency_ms = (
        total_prediction_time / (100 * len(X_test))
    ) * 1000

    predictions = model.predict(X_test)

    results.append({
        "Feature Group": name,
        "Accuracy": accuracy_score(y_test, predictions),
        "Precision": precision_score(y_test, predictions, zero_division=0),
        "Recall": recall_score(y_test, predictions, zero_division=0),
        "F1 Score": f1_score(y_test, predictions, zero_division=0),
        "Training Time (seconds)": training_time,
        "Average Latency (ms/sample)": avg_latency_ms
    })

# Display and save results
results_df = pd.DataFrame(results)

print("\nFEATURE GROUP EXPERIMENT RESULTS")
print(results_df.to_string(index=False))

results_df.to_csv(
    "results/feature_experiment.csv",
    index=False
)

print("\nFeature experiment completed!")
print("Results saved successfully!")
