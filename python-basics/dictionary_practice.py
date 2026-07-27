# =====================================================================
# TOPIC: PYTHON DICTIONARIES (Key-Value Pairs, Methods, Loops & Nesting)
# TOTAL QUESTIONS: 6 (1 Easy, 2 Medium, 3 Hard)
# INSTRUCTIONS: Write your Python code below each comment block.
# =====================================================================

# ---------------------------------------------------------------------
# 🟢 EASY LEVEL
# ---------------------------------------------------------------------

# QUESTION 1: Student Profile Card
# Babar bhai, apne bare mein ek choti dictionary banayein:
# student = {"name": "Babar", "degree": "Data Science", "semester": 2}
# Is dictionary ka istemal karte hue screen par ek 
# saaf suthra message print karein:
# "[name] is studying [degree] in [semester]nd semester."
student = {"name": "Babar", "degree": "Data Science", "semester": 2}
print(student["name"] , " is studying" , student["degree"] , " in" , student["semester"] , " semester.")

# ---------------------------------------------------------------------
# 🟡 MEDIUM LEVEL
# ---------------------------------------------------------------------

# QUESTION 2: Sabzi Mandi Inventory Manager
# Ek dukan par sabziyon ka stock mojud hai:
# stock = {"Aloo": 50, "Piyaz": 30, "Tamatar": 20}
# 1. "Aloo" ka stock update kar ke 80 kg kar dein.
# 2. Ek nayi sabzi "Matar" dalein jis ka stock 15 kg ho.
# Final updated dictionary ko screen par print karein.
stock = {"Aloo": 50, "Piyaz": 30, "Tamatar": 20}
print("Purana alo stock = " , stock["Aloo"])
stock["Aloo"] = 80
print("New alo stock = " , stock["Aloo"])
stock["Matar"] = 15
print(stock)

# QUESTION 3: Safe Price Lookup (The .get() Method)
# Ek hotel ka menu mojud hai: menu = {"Chai": 50, "Samosa": 30}
# User se ek item ka naam input lein (e.g., "Chai" ya "Burger").
# Menu se price nikalne ke liye .get() method ka use karein
# taake agar user "Burger" likhe (jo menu mein nahi hai),
# to error aane ki bajaye "Item available nahi hai" print ho.
menu = {"Chai": 50, "Samosa": 30}
user = input("Enter a name: ")
print(menu.get(user,"Item available nahi hay."))

# ---------------------------------------------------------------------
# 🔴 HARD LEVEL
# ---------------------------------------------------------------------

# QUESTION 4: Shopping Cart Bill Calculator
# Dukan ke rates hain: prices = {"Doodh": 200, "Anda": 30, "Bread": 100}
# User ne ye cheezein khareedin: cart = ["Doodh", "Bread", "Doodh"]
# Ek variable banayein: total_bill = 0
# For loop chalakar cart ke ek ek item par jayein,
# prices dictionary se uski keemat nikal kar total mein plus karein.
# End mein kul bill screen par show karein.
prices = {"Doodh": 200, "Anda": 30, "Bread": 100}
cart = ["Doodh", "Bread", "Doodh"]
total_bill = 0
for c in cart:
    price = prices[c]
    total_bill += price
print("Total bill = ", total_bill)

# QUESTION 5: Fruit Frequency Counter (Dynamic Dict)
# Ek tokri mein boht se phal hain: 
# basket = ["Aam", "Kela", "Aam", "Seb", "Kela", "Aam"]
# Ek khali dictionary banayein: fruit_count = {}
# Loop chalayein, agar phal pehle se dictionary mein hai to count + 1
# karein, warna us phal ko dictionary mein 1 value ke sath add karein.
# End mein dikhaein ke kaunsa phal kitni dafa aaya.
basket = ["Aam", "Kela", "Aam", "Seb", "Kela", "Aam"]
fruit_count = {}

for fruit in basket:
    if fruit in fruit_count:
        fruit_count[fruit] = fruit_count[fruit] + 1 # Ginti ek barha do
    else:
        fruit_count[fruit] = 1 # Pehli dafa aya hai to 1 rakh do
print("Phalon ki ginti:", fruit_count)

# QUESTION 6: University Group Database (Nested Dictionary)
# Aapke project group ka data ek nested dictionary mein hai:
# group = {
#     "Member1": {"name": "Arshma", "role": "Developer"},
#     "Member2": {"name": "Babar", "role": "Leader"}
# }
# Nested keys ka sahi istemal karte hue Member2 ka naam 
# aur uska role alag alag nikal kar screen par print karein.
group = {
    "Member1": {"name": "Arshma", "role": "Developer"},     
    "Member2": {"name": "Babar", "role": "Leader"}
}
print(group["Member2"]["name"])
print(group["Member2"]["role"])