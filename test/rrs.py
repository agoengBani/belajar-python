class Process:
    def __init__(self, name, arrival_time, burst_time):
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time

def round_robin(processes, quantum):
    total_processes = len(processes)
    time = 0
    remaining_processes = total_processes
    queue = []

    while remaining_processes > 0:
        for process in processes:
            if process.arrival_time <= time and process not in queue and process.remaining_time > 0:
                queue.append(process)

        if len(queue) == 0:
            time += 1
            continue

        current_process = queue.pop(0)
        print("Time", time, "-", time + min(quantum, current_process.remaining_time), ":", current_process.name)

        if current_process.remaining_time <= quantum:
            time += current_process.remaining_time
            current_process.remaining_time = 0
            remaining_processes -= 1
        else:
            time += quantum
            current_process.remaining_time -= quantum

        for process in processes:
            if process != current_process and process.arrival_time <= time and process.remaining_time > 0 and process not in queue:
                queue.append(process)

def main():
    processes = [
        Process("P1", 0, 10),
        Process("P2", 1, 4),
        Process("P3", 2, 5),
        Process("P4", 3, 3)
    ]
    quantum = 2
    print("Round-Robin Scheduling:")
    round_robin(processes, quantum)

if __name__ == "__main__":
    main()
