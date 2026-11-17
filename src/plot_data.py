
import pandas as pd
import matplotlib.pyplot as plt

# Read the generated dataset
df = pd.read_csv("data/normal_data.csv")

# Create water tank graph
plt.figure(figsize=(10, 5))

plt.plot(
    df["time"],
    df["water_level"],
    marker=".",
    label="Water Level"
)

plt.axhline(
    y=80,
    linestyle="--",
    label="Valve Close Level"
)

plt.axhline(
    y=30,
    linestyle="--",
    label="Valve Open Level"
)

plt.title("Digital Twin - Water Tank Simulation")
plt.xlabel("Time (Seconds)")
plt.ylabel("Water Level (%)")

plt.legend()
plt.grid(True)

plt.savefig("figures/water_tank_graph.png")
plt.show()

print("Graph saved successfully!")
