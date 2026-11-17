
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 1. Load dataset
df = pd.read_csv("data/combined_dataset.csv")

# 2. Handle missing values
df["anomaly_type"] = df["anomaly_type"].fillna("None")

# 3. Encode categorical features
df["valve_status"] = df["valve_status"].map({
    "OPEN": 1,
    "CLOSED": 0
})

# 4. Separate features and target
X = df[["water_level", "flow_rate", "valve_status"]]
y = df["status"].map({
    "Normal": 0,
    "Anomaly": 1
})

# 5. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# 6. Feature scaling
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 7. Display results
print("Preprocessing Completed Successfully!")

print("\nOriginal Dataset:", df.shape)
print("Training Features:", X_train.shape)
print("Testing Features:", X_test.shape)

print("\nTraining Labels:")
print(y_train.value_counts())

print("\nTesting Labels:")
print(y_test.value_counts())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nFeature Scaling Completed!")
