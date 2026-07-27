# =====================================================================
# TOPIC: ASYNC PYTHON (asyncio, async/await, gather, and Timeouts)
# TOTAL QUESTIONS: 6 (1 Easy, 2 Medium, 3 Hard)
# INSTRUCTIONS: Write your Python code below each comment block.
# =====================================================================

import asyncio
import time

# ---------------------------------------------------------------------
# 🟢 EASY LEVEL
# ---------------------------------------------------------------------

# QUESTION 1: The Simple File Downloader (async/await Basics)
# `async def` ka use kar ke ek function banayein: `download_file()`.
# Iske andar print karein "Download shuru ho gaya...".
# Phir `await asyncio.sleep(2)` ka use kar ke 2 seconds ka break lagayein
# (jo simulate karega ke file download ho rahi hai).
# Aakhir mein print karein "Download Mukammal! 💾".
# Main thread mein `asyncio.run()` ke zariye isay chalaein.
import asyncio
import time
async def download_file():
    print("Download shuru..")
    await asyncio.sleep(2)
    print("Download khtm..")
asyncio.run(download_file())

# ---------------------------------------------------------------------
# 🟡 MEDIUM LEVEL
# ---------------------------------------------------------------------

# QUESTION 2: University Portal Dashboard (Parallel Tasks with gather)
# Dashboard load karte waqt do alag alag cheezein internet se aani hain:
# 1. `fetch_attendance()` -> Isme 1 second ka async sleep ho.
# 2. `fetch_grades()` -> Isme 2 seconds ka async sleep ho.
# Dono functions data return karein. Ek teesra main function banayein
# jo `asyncio.gather()` ka use kar ke dono ko EK SATH (parallel) chalaye.
# Total time check karein ke kya dono 2 seconds mein load hote hain ya 3 mein!
import asyncio
import time
async def fetch_attendence():
    print("Fetching Attendence..")
    await asyncio.sleep(1)
    print("Fetched Attendence..")
async def fetch_grades():
    print("Fetching Grades..")
    await asyncio.sleep(2)
    print("Fetched Grades..")
async def main():
    await asyncio.gather(fetch_attendence(),fetch_grades())
asyncio.run(main())

# QUESTION 3: Database Query Guard (Async Timeouts)
# Ek async function banayein: `heavy_sql_query()`. Inside it, 
# 4 seconds ka `asyncio.sleep` lagayein (mushkil query simulation).
# Hamein is query par guard lagana hai ke agar yeh 2 seconds se zyada 
# waqt le, to system crash na ho balkay timeout ho jaye.
# `asyncio.wait_for()` ka use kar ke 2 seconds ka limit lagayein
# aur `TimeoutError` ko try-except block se handle kar ke message dikhaein.
import asyncio
import time
async def heavy_sql_query():
    print("Db say conect kr rha hun..")
    await asyncio.sleep(4)
    print("Connect ho gya..")
async def main():
    try:
        async with asyncio.timeout(2):
            res = await heavy_sql_query()
            return res
    except TimeoutError:
        print("Bhai 2 seconds guzr gye, ab kam khatm. phir try kro.")
asyncio.run(main())


# ---------------------------------------------------------------------
# 🔴 HARD LEVEL
# ---------------------------------------------------------------------

# QUESTION 4: Background Log Processor (Creating Tasks)
# Kabhi kabhi hum chahte hain ke main code chalta rahe aur piche background 
# mein koi kaam shuru ho jaye. Ek function banayein `background_logger()`.
# Yeh function 3 seconds tak piche logs save kare.
# Main function mein `asyncio.create_task(background_logger())` chalayein.
# Aur uske foran baad main function apna aik alag print statement chalaye.
# Output mein dekhein ke kya main function background task ka wait kiye bina agay nikalta hai?
import  asyncio
async def back_lodger():
    print("Log save krna start..")
    await asyncio.sleep(3)
    print("Kam khatm o gya j..")
async def main():
    print("Main start..")
    task = asyncio.create_task(back_lodger())
    print("Bhai dojy kam kar rya j wait kro..")
    await asyncio.sleep(4)
    await task
    print("Main v khatm")
asyncio.run(main())

# QUESTION 5: Smart Web Scraper Pipeline (Async with Exception Handling)
# Data Science ke liye 3 websites se data scrape karna hai: ["UOG", "HEC", "Google"].
# Ek async function banayein `scrape_website(site)`. 
# Agar site ka naam "HEC" ho, to jaan boojh kar `ValueError("Network Error")` raise karein.
# Warna normal scraping successfully print karein.
# Main function mein `asyncio.gather()` ka use karte hue teeno sites ko ek sath bhejin
# aur `return_exceptions=True` param lagayein taake galti baki 2 sites ka data kharab na kare.
import asyncio 
import time
webs = ["UOG", "HEC", "Google"]
async def scrape_webs(web):
    if web == "HEC":
        raise ValueError("Network error a gya j sir")
    await asyncio.sleep(1)
    print(web, ' Scraped successfuly.')
async def main():
    try:
        await asyncio.gather(*(scrape_webs(webs[0]),scrape_webs(webs[1]),scrape_webs(webs[2])), return_exceptions = True)
    except Exception as e:
        print("Error : " , e)
asyncio.run(main())

import asyncio

async def scrape_website(site):
    if site == "HEC":
        raise ValueError("HEC Server Down! Network Error")
    await asyncio.sleep(1)
    return f"{site} Data Scraped Successfully"

async def main():
    sites = ["UOG", "HEC", "Google"]
    
    # return_exceptions=True ka jadu yeh hai ke ek error se poora batch kharab nahi hota
    results = await asyncio.gather(*(scrape_website(s) for s in sites), return_exceptions=True)
    
    for res in results:
        if isinstance(res, Exception):
            print(f"Caught an Error: {res}")
        else:
            print("Success:", res)

asyncio.run(main())
# QUESTION 6: Graceful Project Dashboard Shutdown (Task Cancellation)
# Ek infinite async loop function banayein: `refresh_dashboard()`.
# Yeh function har 0.5 second baad "Dashboard refreshing..." print karta rahe.
# Main function mein is task ko `create_task()` se background mein on karein.
# Main function khud 2 seconds tak soye (`await asyncio.sleep(2)`),
# aur uske baad `task.cancel()` ka jadui button daba kar background function ko
# tameez se band kar de. Cancel hone par `asyncio.CancelledError` pakar kar check karein.
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