
# FCFS CPU Scheduling Simulation

processes = [
    {"Process": "P1", "Arrival Time": 0, "Burst Time": 5},
    {"Process": "P2", "Arrival Time": 1, "Burst Time": 3},
    {"Process": "P3", "Arrival Time": 2, "Burst Time": 4},
    {"Process": "P4", "Arrival Time": 3, "Burst Time": 2}
]

current_time = 0
total_waiting_time = 0
total_turnaround_time = 0

print("FCFS CPU SCHEDULING SIMULATION\n")

print("Process | Arrival | Burst | Waiting | Turnaround")

for process in processes:
    arrival = process["Arrival Time"]
    burst = process["Burst Time"]

    if current_time < arrival:
        current_time = arrival

    waiting_time = current_time - arrival
    current_time += burst

    turnaround_time = current_time - arrival

    total_waiting_time += waiting_time
    total_turnaround_time += turnaround_time

    print(
        f'{process["Process"]:7} | '
        f'{arrival:7} | '
        f'{burst:5} | '
        f'{waiting_time:7} | '
        f'{turnaround_time:10}'
    )

count = len(processes)

print("\nAverage Waiting Time:",
      round(total_waiting_time / count, 2))

print("Average Turnaround Time:",
      round(total_turnaround_time / count, 2))

print("\nFCFS Scheduling Completed!")
