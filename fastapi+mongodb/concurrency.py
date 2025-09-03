import asyncio
import random

async def fetch_data(task_id):
    delay = random.uniform(1, 3)
    print(f"Task {task_id}: Starting fetch, will take {delay:.2f} seconds...")
    await asyncio.sleep(delay)
    print(f"Task {task_id}: Finished fetch!")
    return f"Data from task {task_id}"

async def main_sequential():
    print("Starting tasks sequentially...")
    results = []
    for i in range(1, 6):
        data = await fetch_data(i)  # Waits for this task to finish before next starts
        results.append(data)
    print("Sequential results:", results)

asyncio.run(main_sequential())
