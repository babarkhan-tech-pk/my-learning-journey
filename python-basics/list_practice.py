# =====================================================================
# TOPIC: PYTHON LISTS (Creation, Indexing, Methods & Slicing)
# TOTAL QUESTIONS: 6 (1 Easy, 2 Medium, 3 Hard)
# INSTRUCTIONS: Write your Python code below each comment block.
# =====================================================================

# ---------------------------------------------------------------------
# 🟢 EASY LEVEL
# ---------------------------------------------------------------------

# QUESTION 1: The Fruit Basket Indexer
# Aapke paas ek pakooray aur phalon ki list hai:
# items = ["Aam", "Kela", "Seb", "Aroo", "Tarbooz"]
# Aapne is list se pehla phal (First Item) aur 
# aakhri phal (Last Item) nikal kar screen par 
# print karna hai index ka istemal kar ke.
items = ["Aam", "Kela", "Seb", "Aroo", "Tarbooz"]
print[items[0]]
print(items[4])

# ---------------------------------------------------------------------
# 🟡 MEDIUM LEVEL
# ---------------------------------------------------------------------

# QUESTION 2: Birthday Guest List Manager
# Ammi ne kaha ke birthday par dosto ko bulana hai.
# Pehle se aik list bani hai: guests = ["Ali", "Zain", "Raza"]
# 1. append() ka use kar ke "Babar" ko list mein shamil karein.
# 2. remove() ka use kar ke "Raza" ko list se nikal dein 
# kyunki wo shehar se bahar gaya hua hai.
# Final updated list ko screen par print karein.
guests = ["Ali", "Zain", "Raza"]
print(guests)
guests.append("Babar")
print(guests)
guests.remove("Raza")
print(guests)

# QUESTION 3: Cricket Match Overs Slicing
# Ek bowler ne 6 overs mein ye runs diye: runs = [4, 12, 8, 2, 15, 6]
# Python ki Slicing [start:stop] ka jadu use karein aur:
# Pehle 3 overs ke runs alag kar ke ek nayi list banayein.
# Phir aakhri 2 overs ke runs alag kar ke doosri list banayein.
# Dono nayi lists ko screen par show karein.
runs = [4, 12, 8, 2, 15, 6]
half1 = runs[0:3]
half2 = runs[4:6]
print(runs)
print(half1)
print(half2)

# ---------------------------------------------------------------------
# 🔴 HARD LEVEL
# ---------------------------------------------------------------------

# QUESTION 4: Fitness Step Tracker Filter
# Ek fit bande ne poore hafte ke steps record kiye:
# weekly_steps = [4000, 7500, 3000, 9000, 11000, 5000, 8500]
# Ek khali list banayein: good_days = []
# Loop aur IF condition chalakar sirf wo steps "good_days" 
# mein append karein jo 7000 se zyada (yani > 7000) hain.
# End mein "good_days" ki list print karein.
weekly_steps = [4000, 7500, 3000, 9000, 11000, 5000, 8500]
good_days = []
for step in weekly_steps:
    if step > 7000:
        good_days.append(step)
print(weekly_steps)
print(good_days)

# QUESTION 5: School Exam Pass/Fail Segregator
# Ek teacher ke paas class ke marks hain: marks = [35, 65, 42, 88, 92, 25]
# Do alag khali lists banayein: "pass_students" aur "fail_students".
# Loop chalayein, agar marks 50 ya us se zyada hain to pass wali list
# mein dalein, warna fail wali list mein dalein.
# Dono lists ko alag alag saaf suthra print karein.
marks = [35, 65, 42, 88, 92, 25]
pass_students = []
fail_students = []
for mark in marks:
    if mark >= 50:
        pass_students.append(mark)
    else:
        fail_students.append(mark)
print(marks)
print(pass_students)
print(fail_students)

# QUESTION 6: Duplicate Item Remover (Unique Cart)
# Shopping cart mein user ne galti se kuch cheezein do dafa daal dein:
# cart = ["Doodh", "Anda", "Doodh", "Bread", "Anda", "Chini"]
# Ek khali list banayein: unique_cart = []
# Loop chalayein aur check karein, agar item pehle se "unique_cart" 
# mein MAJOOD NAHI HAI (not in keyword use karein), to hi usay dalein.
# Is tarah saari duplicate cheezein saaf ho jani chahiye!
cart = ["Doodh", "Anda", "Doodh", "Bread", "Anda", "Chini"]
unique_cart = []
for item in cart:
    if item not in unique_cart:
        unique_cart.append(item)
print(cart)
print(unique_cart)