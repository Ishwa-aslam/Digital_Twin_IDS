import random
import pandas as pd


class WaterTank:

    def __init__(self):
        self.water_level = 50.0
        self.valve_status = "OPEN"

    def update(self):

        if self.water_level >= 80:
            self.valve_status = "CLOSED"

        elif self.water_level <= 30:
            self.valve_status = "OPEN"

        if self.valve_status == "OPEN":
            self.water_level += random.uniform(1, 3)
        else:
            self.water_level -= random.uniform(0.5, 1.5)

        self.water_level = max(0, min(100, self.water_level))

    def get_sensor_reading(self):
        return round(self.water_level, 2)


# --------------------------------
# 1. Generate Normal Dataset
# --------------------------------

tank = WaterTank()
normal_records = []

for second in range(100):

    tank.update()
    reading = tank.get_sensor_reading()

    if tank.valve_status == "OPEN":
        flow_rate = round(random.uniform(8, 12), 2)
    else:
        flow_rate = round(random.uniform(0, 1), 2)

    normal_records.append({
        "time": second,
        "water_level": reading,
        "flow_rate": flow_rate,
        "valve_status": tank.valve_status,
        "status": "Normal",
        "anomaly_type": "None"
    })


normal_df = pd.DataFrame(normal_records)
normal_df.to_csv("data/normal_data.csv", index=False)


# --------------------------------
# 2. Generate Simulated Anomalies
# --------------------------------

abnormal_records = []

for second in range(100):

    base = normal_records[second].copy()

    anomaly = random.choice([
        "Sensor Spike",
        "Abnormal Flow",
        "Valve Mismatch"
    ])

    if anomaly == "Sensor Spike":

        base["water_level"] += random.choice([-25, 25])
        base["water_level"] = max(
            0, min(100, base["water_level"])
        )

    elif anomaly == "Abnormal Flow":

        base["flow_rate"] = round(random.uniform(18, 25), 2)

    elif anomaly == "Valve Mismatch":

        if base["valve_status"] == "OPEN":
            base["valve_status"] = "CLOSED"
        else:
            base["valve_status"] = "OPEN"

    base["status"] = "Anomaly"
    base["anomaly_type"] = anomaly

    abnormal_records.append(base)


abnormal_df = pd.DataFrame(abnormal_records)
abnormal_df.to_csv("data/abnormal_data.csv", index=False)


# --------------------------------
# 3. Display Results
# --------------------------------

print("Normal Dataset Generated:", len(normal_df), "records")
print("Abnormal Dataset Generated:", len(abnormal_df), "records")

print("\nAnomaly Distribution:")
print(abnormal_df["anomaly_type"].value_counts())

print("\nBoth datasets saved successfully!")