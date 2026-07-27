# =====================================================================
# TOPIC: PYTHON FUNCTIONS (def Keyword, Arguments, Return Values & Scope)
# TOTAL QUESTIONS: 6 (1 Easy, 2 Medium, 3 Hard)
# INSTRUCTIONS: Write your Python code below each comment block.
# =====================================================================

# ---------------------------------------------------------------------
# 🟢 EASY LEVEL
# ---------------------------------------------------------------------

# QUESTION 1: University Gate Welcome Board
# University of Gujrat ke gate par ek digital board laga hai.
# `def` ka use kar ke `welcome_student(name)` naam ka function banayein.
# Yeh function parameter mein bache ka naam lega, aur screen par
# print karega: "Welcome to UOG, [name]! Aapka din acha guzre. 🎓"
# Function banane ke baad usay "Babar" naam de kar call bhi karein.
def welcome_student(name):
    print(f"Welcome to UOG, {name}! Aapka din acha guzre.")
welcome_student("Babar")
welcome_student("Ali")

# ---------------------------------------------------------------------
# 🟡 MEDIUM LEVEL
# ---------------------------------------------------------------------

# QUESTION 2: Ammi's Samosa Bill Calculator (Using Return)
# Ammi ne dukan se samosay mangwaye hain. Ek function banayein:
# `calculate_samosa_bill(price, quantity)`
# Yeh function dono cheezon ko multiply karega aur total bill ko 
# print nahi karega, balkay `return` keyword se wapas bhejega.
# Baahir ek variable mein return hui value save karein aur print karein.
def calculate_samosa_bill(price, quantity):
    return price * quantity
bill1 = calculate_samosa_bill(10,5)
print("Bill 1 = " , bill1)
bill2 = calculate_samosa_bill(20,15)
print("Bill 2 = " , bill2)

# QUESTION 3: Fitness Tracker (Steps to KM Converter)
# Ek fitness tracker app ke liye function banayein: `steps_to_km(steps)`
# Farz karein 1300 steps chalne se 1 kilometer banta hai.
# Yeh function total steps ko 1300 se divide karega aur 
# jo kilometers (float value) aayenge, unhein return karega.
# Function ko 5200 steps de kar check karein ke kitne KM bante hain.
def steps_to_km(steps):
    return steps / 1300
chk_steps = steps_to_km(5200)
print(chk_steps)

# ---------------------------------------------------------------------
# 🔴 HARD LEVEL
# ---------------------------------------------------------------------

# QUESTION 4: Wapda Electricity Bill Slabs (Logic inside Function)
# Bijli ka bill calculate karne ke liye ek advanced function banayein:
# `calculate_electricity_bill(units)`
# If-else ka use karein: Agar units 100 ya us se kam hain, to rate 
# 15 rupees per unit hoga. Agar units 100 se zyada hain, to pehle 
# 100 units ka rate 15 hoga aur baqi oopar wale units ka rate 25 hoga.
# Total bill calculate kar ke return karein aur baahir test karein.
def calculate_electricity_bill(units):
    if units <= 100:
        return units * 15
    else:
        return units * 25
print(calculate_electricity_bill(90))
print(calculate_electricity_bill(190))

# QUESTION 5: Project Task Assigner (Default Arguments)
# Data science project ke liye ek function banayein:
# `assign_task(task_name, member_name="Babar")`
# Ghaur se dekhein, member_name ki default value "Babar" rakhi hai.
# Agar function call karte waqt koi naam na diya jaye, to screen par
# print ho: "[task_name] task is assigned to Leader Babar."
# Agar koi aur naam diya jaye (e.g. "Arshma"), to uske naam se print ho.
def assign_task(task_name, member_name="Babar"):
    print(task_name , " Task is assigned to team leader " , member_name)
assign_task("Documentation")
assign_task("Coding","Ali")

# QUESTION 6: Smart ATM Tax Deductor (Multiple Return Values)
# ATM machine se paise nikalwane par 2% tax kat ta hai. Function banayein:
# `withdraw_cash(amount)`
# Yeh function amount ka 2% tax nikalega (tax = amount * 0.02).
# Phir ye function EK SATH DO CHEEZEIN return karega:
# Bachi hui asli rakam (amount - tax) AUR kata hua tax.
# Baahir tuple unpacking ka use kar ke dono values alag alag print karein.
def withdraw_cash(amount):
    tax = amount * 0.02
    amount = amount - tax
    return (tax,amount)
cash1 = withdraw_cash(1000)
print("Tax = ", cash1[0] , " , Withdarwan Amount = " , cash1[1] , " , Total amount = " , cash1[0]+cash1[1])
cash2 = withdraw_cash(12738)
print("Tax = ", cash2[0] , " , Withdarwan Amount = " , cash2[1] , " , Total amount = " , cash2[0]+cash2[1])