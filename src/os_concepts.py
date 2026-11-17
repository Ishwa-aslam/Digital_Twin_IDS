
import multiprocessing
import threading

# Shared data for thread demonstration
sensor_logs = []
lock = threading.Lock()


# Process worker function
def process_worker(queue):
    sensor_value = 75
    message = f"Process received sensor value: {sensor_value}"
    queue.put(message)


# Thread worker function
def thread_worker(thread_name):
    for reading in range(1, 4):
        with lock:
            sensor_logs.append({
                "thread": thread_name,
                "reading": reading
            })


def main():
    print("OS Concepts Demonstration Started\n")

    # 1. Process Management + 2. IPC
    print("1. PROCESS MANAGEMENT AND IPC")

    queue = multiprocessing.Queue()

    process = multiprocessing.Process(
        target=process_worker,
        args=(queue,)
    )

    process.start()
    process.join()

    message = queue.get()
    print(message)
    print("Child process completed.\n")

    # 3. Multithreading + 4. Synchronization
    print("2. MULTITHREADING AND SYNCHRONIZATION")

    thread1 = threading.Thread(
        target=thread_worker,
        args=("Thread 1",)
    )

    thread2 = threading.Thread(
        target=thread_worker,
        args=("Thread 2",)
    )

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    for record in sensor_logs:
        print(record)

    print("\nTotal sensor records:", len(sensor_logs))
    print("\nOS Concepts Demonstration Completed!")


if __name__ == "__main__":
    main()
