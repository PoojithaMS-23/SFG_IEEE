import asyncio
import random

async def fetch_data(task_id):
    delay = random.uniform(2, 7)  # Random delay between 0.5 and 3 seconds
    print(f"Task {task_id}: Starting fetch, will take {delay:.2f} seconds...")
    await asyncio.sleep(delay)  # Simulate network I/O or processing delay
    print(f"Task {task_id}: Finished fetch!")
    return f"Data from task {task_id}"

async def process_data(task_id, data):
    delay = random.uniform(3, 7)
    print(f"Task {task_id}: Processing data, will take {delay:.2f} seconds...")
    await asyncio.sleep(delay)  # Simulate processing delay
    print(f"Task {task_id}: Finished processing!")
    return f"Processed {data}"

async def main():
    print("Starting all tasks...")

    # Step 1: Concurrently fetch data from multiple tasks
    fetch_tasks = [fetch_data(i) for i in range(1, 6)]
    fetched_results = await asyncio.gather(*fetch_tasks)

    # Step 2: Process each fetched result concurrently
    process_tasks = [process_data(i+1, data) for i, data in enumerate(fetched_results)]
    processed_results = await asyncio.gather(*process_tasks)

    print("\nAll tasks completed. Results:")
    for result in processed_results:
        print(result)

asyncio.run(main())
