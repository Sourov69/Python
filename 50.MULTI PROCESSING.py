# Multiprocessing in Python refers to a technique used to execute multiple processes or tasks simultaneously, taking advantage of multiple CPU cores. The `multiprocessing` module allows the creation of separate processes, each having its memory space, enabling parallel execution of tasks. It's particularly useful for CPU-bound operations and can significantly speed up the execution of certain types of programs by dividing the workload among different processes

#3 The `multiprocessing` module allows you to create processes, each with its own memory space, enabling parallel execution. Here's an example:


import multiprocessing

# Function to be executed in parallel
def square_numbers(numbers, result, index):
    for i, num in enumerate(numbers):
        result[index + i] = num * num

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    result = multiprocessing.Array('i', len(numbers))  # Shared memory array to store results

    # Splitting the numbers into two separate processes
    mid = len(numbers) // 2
    p1 = multiprocessing.Process(target=square_numbers, args=(numbers[:mid], result, 0))
    p2 = multiprocessing.Process(target=square_numbers, args=(numbers[mid:], result, mid))

    # Start the processes
    p1.start()
    p2.start()

    # Wait for both processes to complete
    p1.join()
    p2.join()

    # Output the squared numbers
    print(list(result))