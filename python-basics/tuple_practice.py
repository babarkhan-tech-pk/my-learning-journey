# =====================================================================
# TOPIC: PYTHON TUPLES (Immutability, Indexing, Unpacking & Operations)
# TOTAL QUESTIONS: 6 (1 Easy, 2 Medium, 3 Hard)
# INSTRUCTIONS: Write your Python code below each comment block.
# =====================================================================

# ---------------------------------------------------------------------
# 🟢 EASY LEVEL
# ---------------------------------------------------------------------

# QUESTION 1: Fixed GPS Coordinates
# Aap ek Google Maps ki tarah ki app bana rahe hain.
# Kharian shehar ke fixed GPS coordinates ka tuple banayein:
# coordinates = (32.8114, 73.8651)
# Is tuple se Latitude (pehla number) aur Longitude
# (doosra number) alag alag variable mein nikal kar
# index ki madad se screen par print karein.
coordinates = (32.8114, 73.8651)
latitude = coordinates[0]
langitude = coordinates[1]
print("Latitude = " , latitude)
print("Langitude = " , langitude)

# ---------------------------------------------------------------------
# 🟡 MEDIUM LEVEL
# ---------------------------------------------------------------------

# QUESTION 2: Movie Data Unpacking
# Ek website par film ka data tuple mein save hai:
# movie_data = ("The Legend of Maula Jatt", 2022, 9.2)
# Python ke "Tuple Unpacking" ka jadu istemal karein.
# Ek hi line mein teeno cheezon ko teen alag variables
# (title, year, rating) mein band karein.
# Phir un variables ko saaf suthra print karein.
movie_data = ("The Legend of Maula Jatt", 2022, 9.2)
title,year,rating = movie_data
print("Movie title = " , title)
print("Movie year = " , year)
print("Movie rating = " , rating)

# QUESTION 3: Traffic License Test Analyzer
# Ek driving test mein user ke answers ka tuple bana hai:
# answers = ("Pass", "Fail", "Pass", "Pass", "Fail")
# Tuple ke methods ka istemal kar ke do cheezein pata karein:
# 1. User ne kul kitni dafa "Pass" hasil kiya (count() use karein).
# 2. Pehli dafa "Fail" kis index par aaya (index() use karein).
answers = ("Pass", "Fail", "Pass", "Pass", "Fail")
count = 0
for a in answers:
    if a == "Pass":
        count += 1
    else:
        print(answers.index(a))
print("Total pass = " , count)

# ---------------------------------------------------------------------
# 🔴 HARD LEVEL
# ---------------------------------------------------------------------

# QUESTION 4: The Locked Software Settings (Immutability Hack)
# Ek software ki settings locked hain: settings = ("Urdu", "Dark", 80)
# Aapne is settings mein volume ko 80 se badal kar 100 karna hai.
# Kyunki tuple direct change nahi ho sakta, is liye:
# Pehle tuple ko list() lagakar list mein badlein.
# Phir volume badlein, aur dobara tuple() lagakar block karein.
# Final locked tuple ko screen par dikhaein.
settings = ("Urdu", "Dark", 80)
print("Before change = " , type(settings))
temp_list = list(settings)
temp_list[2] = 100
print("After change 1 = " , type(temp_list))
settings = tuple(temp_list)
print("After change 2 = " , type(settings))
print(settings)

# QUESTION 5: Supermarket Fruit Bill (List of Tuples)
# Billing counter par items tuples ki shakl mein ek list mein hain:
# cart = [("Seb", 200), ("Kela", 120), ("Aam", 300)]
# Har tuple mein pehla naam hai aur doosri keemat (price) hai.
# Ek total_bill = 0 ka variable banayein.
# Loop chalakar har tuple se price nikalein aur total mein plus karein.
# End mein kul bill screen par show karein.
cart = [("Seb", 200), ("Kela", 120), ("Aam", 300)]
total_bill = 0
for prod in cart:
    name , price = prod
    total_bill += int(price)
print("Total bill = ",total_bill)

# QUESTION 6: Nested Tuple Explorer (Secret Code)
# Ek company ke employee ka advanced data nested tuple mein hai:
# emp_data = ("Babar", ("Data Science", "2nd Semester"), "Kharian")
# Gaur se dekhein, index 1 par ek aur tuple mojud hai.
# Nested indexing ka sahi istemal karte hue sirf bache ka
# department ("Data Science") nikal kar print karein.
emp_data = ("Babar", ("Data Science", "2nd Semester"), "Kharian")
dept_data = emp_data[1]
print("Department = ",dept_data[0])