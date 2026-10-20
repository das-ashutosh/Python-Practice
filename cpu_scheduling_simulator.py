```python
# CPU Scheduling Simulator - FCFS Algorithm

def fcfs_scheduling(processes):
    current_time = 0
    total_waiting = 0
    total_turnaround = 0

    print("\n===== SCHEDULING RESULTS =====")
    print("PID\tArrival\tBurst\tWaiting\tTurnaround")

    for process in sorted(
        processes,
        key=lambda p: (p["arrival"], p["pid"])
    ):
        arrival = process["arrival"]
        burst = process["burst"]

        # CPU waits if the next process has not arrived
        start_time = max(current_time, arrival)
        completion = start_time + burst

        waiting = start_time - arrival
        turnaround = completion - arrival

        total_waiting += waiting
        total_turnaround += turnaround
        current_time = completion

        print(
            f'{process["pid"]}\t{arrival}\t{burst}\t'
            f'{waiting}\t{turnaround}'
        )

    count = len(processes)

    print(f"\nAverage waiting time: {total_waiting / count:.2f}")
    print(f"Average turnaround time: {total_turnaround / count:.2f}")


def main():
    processes = []

    print("===== FCFS CPU SCHEDULING SIMULATOR =====")

    try:
        count = int(input("Number of processes: "))

        if count <= 0:
            print("Enter at least one process.")
            return

        for i in range(1, count + 1):
            print(f"\nProcess P{i}")
            arrival = int(input("Arrival time: "))
            burst = int(input("Burst time: "))

            if arrival < 0 or burst <= 0:
                print("Arrival must be >= 0 and burst must be > 0.")
                return

            processes.append({
                "pid": f"P{i}",
                "arrival": arrival,
                "burst": burst
            })

        fcfs_scheduling(processes)

    except ValueError:
        print("Please enter valid whole numbers.")


if __name__ == "__main__":
    main()
```
