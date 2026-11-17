
import psutil
import pandas as pd

records = []

print("Operating System Monitoring Started\n")

for second in range(20):

    cpu = psutil.cpu_percent(interval=0.5)
    memory = psutil.virtual_memory().percent

    records.append({
        "time": second,
        "cpu_usage": cpu,
        "memory_usage": memory
    })

    print(
        f"Time: {second}s | "
        f"CPU: {cpu}% | "
        f"RAM: {memory}%"
    )

df = pd.DataFrame(records)

df.to_csv("logs/os_monitoring.csv", index=False)

print("\nOS Monitoring Completed!")
print("Log saved successfully!")
