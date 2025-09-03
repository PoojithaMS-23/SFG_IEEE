import asyncio

async def say_after(delay, message):
    await asyncio.sleep(delay)  # Simulate I/O or delay
    print(message)

async def main():
    print("Started")
    await say_after(2, "Hello after 2 seconds")
    await say_after(1, "Hello after 1 second")
    print("Finished")

asyncio.run(main())
