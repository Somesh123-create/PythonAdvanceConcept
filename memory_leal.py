import tracemalloc
import gc
import psutil
import time
from datetime import datetime

def get_memory_info():
    process = psutil.Process()
    mem_info = process.memory_info()
    return {
        'rss': mem_info.rss,
        'vms': mem_info.vms,
        'percent': process.memory_percent()
    }

def monitor_memory():
    tracemalloc.start()
    initial_snapshot = tracemalloc.take_snapshot()
    initial_memory = get_memory_info()

    time.sleep(10)  # Run the application for a certain period

    final_snapshot = tracemalloc.take_snapshot()
    final_memory = get_memory_info()
    top_stats = final_snapshot.compare_to(initial_snapshot, 'lineno')

    return initial_memory, final_memory, top_stats

def clear_memory():
    gc.collect()

def generate_report(initial_memory, final_memory, top_stats, report_file='memory_report.txt'):
    with open(report_file, 'w') as report:
        report.write(f"Memory Report - {datetime.now()}\n\n")
        report.write("Initial Memory Usage:\n")
        report.write(f"RSS: {initial_memory['rss']} bytes\n")
        report.write(f"VMS: {initial_memory['vms']} bytes\n")
        report.write(f"Percent: {initial_memory['percent']}%\n\n")

        report.write("Final Memory Usage:\n")
        report.write(f"RSS: {final_memory['rss']} bytes\n")
        report.write(f"VMS: {final_memory['vms']} bytes\n")
        report.write(f"Percent: {final_memory['percent']}%\n\n")

        report.write("[ Top 10 Memory Usage Differences ]\n")
        for stat in top_stats[:10]:
            report.write(f"{stat}\n")

        report.write("\n")

def main():
    initial_memory, final_memory, top_stats = monitor_memory()

    print("Memory usage before cleanup:")
    print(f"RSS: {initial_memory['rss']} bytes")
    print(f"VMS: {initial_memory['vms']} bytes")
    print(f"Percent: {initial_memory['percent']}%")

    clear_memory()
    final_memory_after_cleanup = get_memory_info()

    print("Memory usage after cleanup:")
    print(f"RSS: {final_memory_after_cleanup['rss']} bytes")
    print(f"VMS: {final_memory_after_cleanup['vms']} bytes")
    print(f"Percent: {final_memory_after_cleanup['percent']}%")

    generate_report(initial_memory, final_memory, top_stats)
    print("Memory report generated.")

if __name__ == "__main__":
    main()
