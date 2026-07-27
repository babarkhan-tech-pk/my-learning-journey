# =====================================================================
# TOPIC: PYTHON GENERATORS (yield Keyword, next() Function & Memory Efficiency)
# TOTAL QUESTIONS: 6 (1 Easy, 2 Medium, 3 Hard)
# INSTRUCTIONS: Write your Python code below each comment block.
# =====================================================================

# ---------------------------------------------------------------------
# 🟢 EASY LEVEL
# ---------------------------------------------------------------------

# QUESTION 1: The Token Token Machine (Simple Generator)
# `def token_generator()` naam ka ek simple generator banayein.
# Iske andar teen dafa `yield` ka use kar ke baari baari
# teen strings return karein: "Token 1", "Token 2", aur "Token 3".
# Baahir iska ek object banayein aur `next()` function ka 
# use kar ke teeno tokens ko bari bari print karwaein.
import time
def token_genrator():
    yield "Token 1"
    print("Wait..")
    time.sleep(1)
    yield "Token 2"
    print("Wait..")
    time.sleep(1)
    yield "Token 3"
gen = token_genrator()
print(next(gen))
print(next(gen))
print(next(gen))

# ---------------------------------------------------------------------
# 🟡 MEDIUM LEVEL
# ---------------------------------------------------------------------

# QUESTION 2: Rocket Fuel Countdown Generator
# Ek generator function banayein: `countdown_generator(start_num)`.
# While loop ka use karein. Jab tak start_num zero se bada hai,
# tab tak wo number `yield` hota rahe aur har dafa number mein se
# ek minus (-= 1) hota rahe. Baahir is generator par ek 
# aam FOR loop chalayein taake countdown automatic print ho.
def countdown_generator(start_num):
    while (start_num > 0):
        yield start_num
        start_num = start_num - 1
gen = countdown_generator(10)
for i in gen:
    print(next(gen))

# QUESTION 3: Even Bus Numbers Streamer
# Aapke paas ek bari list hai: bus_numbers = [11, 22, 33, 44, 55, 66]
# Ek generator function banayein `stream_even_buses(numbers)`.
# Loop chalayein aur check karein, agar number Even (% 2 == 0) hai,
# to usay foran `yield` kar dein. Baahir generator se ek ek kar ke
# sirf even buses ke numbers nikal kar screen par dikhaein.
bus_numbers = [11, 22, 33, 44, 55, 66]
def stream_even_buses(numbers):
    for bus in numbers:
        if bus % 2 == 0:
            yield bus
        else:
            pass
gen = stream_even_buses(bus_numbers)
for i in stream_even_buses(bus_numbers):
    print(next(stream_even_buses(i)))

# ---------------------------------------------------------------------
# 🔴 HARD LEVEL
# ---------------------------------------------------------------------

# QUESTION 4: Infinite Security Log ID Generator
# Security system ke liye unlimited unique IDs chahiye thin.
# Ek generator banayein `infinite_id_generator()`.
# Isme `while True` (infinite loop) chalayein aur shuruati id = 1000 rakhein.
# Har dafa id ko yield karein aur `id += 1` karte jao.
# Baahir ek for loop chalayein jo is unlimited generator se sirf pehli 
# 5 IDs nikal kar print kare aur phir khud hi `break` ho jaye.
def infinite_id_generator():
    id = 1000
    while True:
        yield id
        id += 1
gen = infinite_id_generator()
for i in range(5):
    print(next(gen))

# QUESTION 5: Big Data Science Row Streamer (Memory Saver Simulation)
# Data science mein millions of rows hoti hain jinhein RAM mein lana mana hai.
# Farz karein aisi 3 rows hain: dataset = ["Row 1: Babar", "Row 2: Arshma", "Row 3: Nida"]
# Ek generator function banayein `dataset_streamer(data_list)`.
# Yeh function data ko memory mein load kiye bina ek ek row yield karega.
# Baahir `next()` ka use kar ke pehli 2 rows nikalein, aur check karein
# ke kya teesri row abhi bhi generator ke andar safe mojud hai ya nahi.
dataset = ["Row 1: Babar", "Row 2: Arshma", "Row 3: Nida"]
def dataset_streamer(data_list):
    for row in data_list:
        yield row
gen = dataset_streamer(dataset)
print("Row 1 = " , next(gen))
print("Row 2 = " , next(gen))
print("Row 3 = " , next(gen))
print("Row 4 = " , next(gen))

# QUESTION 6: Recursive-Style Fibonacci Generator
# Ek advanced generator banayein `fibonacci_generator(limit)`.
# Shuruati do numbers a = 0 aur b = 1 rakhein.
# Jab tak a ki value limit se choti hai, tab tak `a` ko yield karein.
# Aur sath hi seats swap karein: `a, b = b, a + b`.
# Baahir limit 20 de kar saari series screen par chamkaein.
def fibonacci_generator(limit):
    a , b = 0,1
    while a < limit:
        yield a
        a , b = b , a+b
gen = fibonacci_generator(20)
for i in gen:
    print(i)