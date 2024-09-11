# asyncio is a Python library used for writing concurrent code using the `async` and `await` syntax. It enables you to write asynchronous, non-blocking code, allowing tasks to run concurrently, making efficient use of I/O-bound operations. It helps manage and coordinate multiple tasks or coroutines to avoid blocking the execution, improving the efficiency of I/O operations and enhancing the performance of Python programs

import asyncio

async def sample_task(number):
    print(f"Task {number} started")
    await asyncio.sleep(1)  # Simulate an asynchronous operation
    print(f"Task {number} completed")

async def main():
    tasks = [sample_task(i) for i in range(3)]
    await asyncio.gather(*tasks)

asyncio.run(main())