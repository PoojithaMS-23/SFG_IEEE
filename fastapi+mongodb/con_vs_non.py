import asyncio
import random
import time

async def fetch_data(task_id):
    delay = random.uniform(1, 3)
    print(f"Task {task_id}: Starting fetch, will take {delay:.2f} seconds...")
    await asyncio.sleep(delay)
    print(f"Task {task_id}: Finished fetch!")
    return f"Data from task {task_id}"

# Sequential version: tasks run one by one
async def run_sequential():
    print("\nRunning tasks sequentially...")
    results = []
    for i in range(1, 6):
        data = await fetch_data(i)
        results.append(data)
    return results

# Concurrent version: tasks run all at once
async def run_concurrent():
    print("\nRunning tasks concurrently...")
    tasks = [fetch_data(i) for i in range(1, 6)]
    results = await asyncio.gather(*tasks)
    return results

async def main():
    start = time.perf_counter()
    await run_sequential()
    sequential_duration = time.perf_counter() - start
    print(f"Sequential total time: {sequential_duration:.2f} seconds")

    start = time.perf_counter()
    await run_concurrent()
    concurrent_duration = time.perf_counter() - start
    print(f"Concurrent total time: {concurrent_duration:.2f} seconds")

asyncio.run(main())
