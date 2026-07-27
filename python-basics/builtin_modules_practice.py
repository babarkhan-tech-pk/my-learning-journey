# =====================================================================
# TOPIC: IMPORTING BUILT-IN MODULES (math, random, datetime, os, aliases)
# TOTAL QUESTIONS: 6 (1 Easy, 2 Medium, 3 Hard)
# INSTRUCTIONS: Write your Python code below each comment block.
# =====================================================================

# ---------------------------------------------------------------------
# 🟢 EASY LEVEL
# ---------------------------------------------------------------------

# QUESTION 1: The Square Root Calculator (math Module)
# Aap ek advanced math calculator bana rahe hain.
# Python ka pehle se bana hua `math` module import karein.
# User se ek number input lein (e.g., 25 ya 64).
# math module ke `sqrt()` function ka use kar ke 
# us number ka square root (jazar) nikal kar print karein.
from math import sqrt as s
user = float(input("Enter a number : "))
print(f"Square root of {user} is {s(user)}.")

# ---------------------------------------------------------------------
# 🟡 MEDIUM LEVEL
# ---------------------------------------------------------------------

# QUESTION 2: Ludo Dice Roller (random Module)
# Aap dosto ke sath Ludo khel rahe hain aur daana ghum gaya hai.
# Python ka `random` module import karein.
# Is module ke `randint()` function ka use kar ke 1 se 6 tak
# ka koi bhi ek random number generate kar ke screen par 
# dikhaein, taake aapki Ludo ki game rukay na!
from random import randint as r
for i in range(5):
    print(r(1,6))

# QUESTION 3: Digital Digital Watch (datetime Module)
# University assignment ke liye aapko digital watch lagani hai.
# Python ka `datetime` module import karein.
# Is module ke andar se aaj ki tarikh aur is waqt ka 
# bilkul exact time (`datetime.now()`) nikal kar print karein,
# taake bache ko pata chale ke assignment mein kitna waqt baqi hai.
import datetime
print(datetime.datetime.now())

# ---------------------------------------------------------------------
# 🔴 HARD LEVEL
# ---------------------------------------------------------------------

# QUESTION 4: Project Group Leader Picker (Specific Imports & Aliases)
# Apne project group ke 4 dosto ke naamon ki ek list banayein.
# Is baar poora module nahi balkay sirf choice function import karein:
# `from random import choice`
# Sath hi `math` module ko ek naya chota naam (Alias) dein: `import math as m`
# 1. `choice()` ka use kar ke list se ek random group leader select karein.
# 2. `m.pow(2, 3)` ka use kar ke 2 ki power 3 ka jawab bhi print karein.
from random import choice
import math as m
lis = ["Babar","Zeeshan","Arshma","Nida","Qirat"]
print(choice(lis))
print(m.pow(2,3))

# QUESTION 5: Automated Folder Creator (os Module with Exception Handling)
# Data Science ke projects save karne ke liye folder banana hai.
# Python ka `os` module import karein jo computer ke folders control karta hai.
# `os.mkdir("DS_Project")` ka use kar ke ek naya folder banayein.
# Is poore code ko try-except mein wrap karein, taake agar folder 
# pehle se bana ho to FileExistsError pakar kar warning message dein.
try:
    import os as o
    o.mkdir("DS_Project")
except Exception as e:
    print("Something gone wrong.")
    print("Error : " , e)
    print("Error class : " , e.__class__.__name__)

# ---------------------------------------------------------------------
# QUESTION 6: Smart Circle Area Generator (Combining math & random)
# Ek geometrical app ke liye circle (daira) ka Area nikalna hai.
# Formula hota hai: Area = pi * r^2
# 1. `random.randint(1, 10)` se circle ka radius (r) automatic generate karein.
# 2. `math.pi` ka use kar ke pi ki exact value (3.1415...) uthaein.
# Both modules ka use kar ke final Area nikal kar screen par show karein.
import random as r
import math as m
ran = r.randint(1,10)
res = m.pi * ( ran * ran)
print(f"Radius = {ran} , pi = {round(m.pi,2)} , area = {res}")