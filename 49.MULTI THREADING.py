# Multi-threading in Python allows multiple threads within a process to execute concurrently. Threads represent paths of execution, enabling the utilization of multiple CPU cores. However, due to Python's Global Interpreter Lock (GIL), which prevents multiple threads from executing Python bytecode at once, threading in Python is more suitable for I/O-bound tasks rather than CPU-bound tasks.

import threading
import time

# Function to simulate a task
def task(name, delay):
    print(f"Thread {name} starting")
    time.sleep(delay)
    print(f"Thread {name} finished")

# Creating threads
thread1 = threading.Thread(target=task, args=("Thread 1", 2))  # Passing the function and its arguments
thread2 = threading.Thread(target=task, args=("Thread 2", 1))

# Start the threads
thread1.start()
thread2.start()

# Ensure all threads complete before moving forward
thread1.join()
thread2.join()

print("All threads have finished")