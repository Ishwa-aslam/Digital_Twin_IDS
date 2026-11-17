
import time
import psutil
import pandas as pd

from sklearn.model_selection import GroupShuffleSplit
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("data/combined_dataset.csv")

df["valve_status"] = df["valve_status"].map({
    "OPEN": 1,
    "CLOSED": 0
})

X = df[["water_level", "flow_rate", "valve_status"]]
y = df["status"].map({"Normal": 0, "Anomaly": 1})

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

models = {
    "Logistic Regression": make_pipeline(
        StandardScaler(),
        LogisticRegression(max_iter=1000)
    ),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )
}

process = psutil.Process()
results = []

for name, model in models.items():

    memory_before = process.memory_info().rss / (1024 ** 2)
    cpu_before = process.cpu_times()
    
    start = time.perf_counter()
    model.fit(X_train, y_train)
    training_time = time.perf_counter() - start

    start = time.perf_counter()
    predictions = model.predict(X_test)
    inference_time = time.perf_counter() - start

    cpu_after = process.cpu_times()
    memory_after = process.memory_info().rss / (1024 ** 2)

    cpu_time = (
        (cpu_after.user + cpu_after.system)
        - (cpu_before.user + cpu_before.system)
    )

    results.append({
        "Model": name,
        "Training Time (seconds)": training_time,
        "Inference Time (seconds)": inference_time,
        "CPU Time (seconds)": cpu_time,
        "Memory Before (MB)": memory_before,
        "Memory After (MB)": memory_after
    })

results_df = pd.DataFrame(results)

print("\nOS RESOURCE UTILIZATION RESULTS")
print(results_df.to_string(index=False))

results_df.to_csv(
    "results/resource_experiment.csv",
    index=False
)

print("\nResource experiment completed!")
print("Results saved successfully!")
