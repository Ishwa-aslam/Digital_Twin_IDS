
import pandas as pd

# Load both datasets
normal_df = pd.read_csv("data/normal_data.csv")
abnormal_df = pd.read_csv("data/abnormal_data.csv")

# Combine datasets
combined_df = pd.concat(
    [normal_df, abnormal_df],
    ignore_index=True
)
combined_df["anomaly_type"] = combined_df["anomaly_type"].fillna("None")
# Shuffle records
combined_df = combined_df.sample(
    frac=1,
    random_state=42
).reset_index(drop=True)

# Save master dataset
combined_df.to_csv(
    "data/combined_dataset.csv",
    index=False
)

# Display results
print("Combined Dataset Created Successfully!")

print("\nDataset Shape:")
print(combined_df.shape)

print("\nClass Distribution:")
print(combined_df["status"].value_counts())

print("\nDataset Preview:")
print(combined_df.head())

print("\nMissing Values:")
print(combined_df.isnull().sum())
