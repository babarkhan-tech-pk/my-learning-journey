import asyncio
import time
async def refresh_dashboard():
    try:
        while True:
            print("Refreshing Dashboard")
            await asyncio.sleep(1)
    except Exception as e:
        print("Something went wrong..")
        print("Error = " , e)
        print("Error class = " , e.__class__.__name__)
async def create_task():
    print("Wait 2 seconds..")
    await asyncio.sleep(2)
    print("Wait 4 seconds")
    task = asyncio.create_task(refresh_dashboard())
    await task
    print("Task error any lga j..")
    task.cancel()
    await asyncio.sleep(0.5)
asyncio.run(create_task())