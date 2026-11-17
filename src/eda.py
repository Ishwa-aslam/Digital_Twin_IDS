
import pandas as pd
import matplotlib.pyplot as plt

# Load combined dataset
df = pd.read_csv("data/combined_dataset.csv")

# 1. Dataset Information
print("Dataset Information:")
print(df.info())

# 2. Statistical Summary
print("\nStatistical Summary:")
print(df.describe())

# 3. Class Distribution
print("\nClass Distribution:")
print(df["status"].value_counts())

# 4. Anomaly Distribution
print("\nAnomaly Distribution:")
print(df["anomaly_type"].value_counts())

# 5. Water Level Graph
plt.figure(figsize=(9, 5))

for status in df["status"].unique():
    subset = df[df["status"] == status]
    plt.scatter(
        subset["time"],
        subset["water_level"],
        label=status,
        alpha=0.7
    )

plt.title("Water Level: Normal vs Anomaly")
plt.xlabel("Time")
plt.ylabel("Water Level (%)")
plt.legend()
plt.grid(True)

plt.savefig("figures/water_level_comparison.png")
plt.show()

# 6. Class Distribution Graph
df["status"].value_counts().plot(
    kind="bar",
    figsize=(7, 5)
)

plt.title("Normal vs Anomaly Distribution")
plt.xlabel("Class")
plt.ylabel("Number of Records")
plt.xticks(rotation=0)
plt.grid(axis="y")

plt.savefig("figures/class_distribution.png")
plt.show()

print("\nEDA Completed Successfully!")
