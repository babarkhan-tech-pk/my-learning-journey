# =====================================================================
# TOPIC: PYTHON MAP() AND FILTER() FUNCTIONS (With Lambda)
# TOTAL QUESTIONS: 6 (1 Easy, 2 Medium, 3 Hard)
# INSTRUCTIONS: Write your Python code below each comment block.
# =====================================================================

# ---------------------------------------------------------------------
# 🟢 EASY LEVEL
# ---------------------------------------------------------------------

# QUESTION 1: Eidi Doubler Machine (Simple map)
# Eid par bacho ko mili eidi ki ek list hai: eidi = [100, 500, 50, 200]
# Abbu ne khush ho kar sab bacho ki eidi ko double (2x) kar diya hai.
# Python ke map() aur lambda ka use kar ke ek hi line mein
# saari eidi ko 2 se multiply karein aur nayi list bana kar print karein.
eidi = [100, 500, 50, 200]
double_eidi = list (map( lambda x : x * 2 , eidi))
print(double_eidi)

# ---------------------------------------------------------------------
# 🟡 MEDIUM LEVEL
# ---------------------------------------------------------------------

# QUESTION 2: Exam Grace Marks Cleaner (Simple filter)
# Class ke bacho ke marks ki list hai: marks = [35, 65, 42, 88, 15, 92]
# Pass hone ke liye kam az kam 50 marks chahiye.
# Python ke filter() aur lambda ka use kar ke ek chalni lagayein
# jo list mein se sirf PASS hone wale bacho ke marks alag kare.
# Final filtered list ko screen par print karein.
marks = [35, 65, 42, 88, 15, 92]
pass_students = list( filter ( lambda x : x >= 50, marks))
print(pass_students)

# QUESTION 3: Weather Report Celsius to Fahrenheit (Map)
# Kharian shehar ke kuch dino ke temperatures Celsius mein hain:
# temps_celsius = [30, 35, 40, 25]
# Formula use karein: F = (C * 9/5) + 32
# map() aur lambda ka jadu chala kar in sab ko Fahrenheit mein
# badlein aur ek nayi list bana kar screen par show karein.
temps_celsius = [30, 35, 40, 25]
temp_faren = list( map( lambda  c : (c * (9/5)) + 32 , temps_celsius))
print(temp_faren)

# ---------------------------------------------------------------------
# 🔴 HARD LEVEL
# ---------------------------------------------------------------------

# QUESTION 4: Long Name Detector in Project Group (Filter)
# Aapke project group ke members hain: names = ["Babar", "Arshma", "Nida", "Zeeshan"]
# Hamein sirf wo naam chahiye jo boht lambe hain, yani jin ke 
# characters ki lambai 5 se zyada hai (len(name) > 5).
# filter() aur lambda ka use kar ke lambe naamon ka set alag karein
# aur unhein screen par saaf suthra print karwaein.
names = ["Babar", "Arshma", "Nida", "Zeeshan"]
big_names = list( filter ( lambda n: len(n) > 5 , names))
print(big_names)

# QUESTION 5: Supermarket Premium Bill Counter (Chaining Map & Filter)
# Ek supermarket mein items ki prices hain: prices = [50, 120, 300, 80, 500]
# Aapne ek advanced kaam karna hai (Chaining):
# Pehle filter() se sirf wo prices nikalein jo 100 rupees se zyada hain.
# Phir jo jawaab aaye, us par map() chala kar 10% tax plus karein (* 1.10).
# Dono functions ko ek hi line mein jor kar final premium bill dikhaein.
prices = [50, 120, 300, 80, 500]
filter_prices = list ( filter (lambda p : p > 100 , prices))
map_prices = list ( map (lambda p: p + (p * 0.15) , filter_prices))
print("Filter prices : " , filter_prices)
print("Map prices : " , map_prices)

prices = [50, 120, 300, 80, 500]
def filter_prices(item):
    if item > 100:
        return item
    else:
        pass
fl_p = list (filter(filter_prices,prices))
print("Filter prices : " , fl_p)

def cl_tax(items):
    return items + (items * 0.15)
mp_p = str(map(cl_tax,fl_p))
print("Tuple : " , mp_p)

# QUESTION 6: University Database Merit Extractor (List of Dicts)
# Students ka data dictionaries ki list mein mojud hai:
# students = [
#     {"name": "Babar", "gpa": 3.8},
#     {"name": "Zeeshan", "gpa": 2.4},
#     {"name": "Arshma", "gpa": 3.9}
# ]
# 1. filter() lagakar sirf wo dicts bachaayein jahan gpa >= 3.5 ho.
# 2. Phir map() lagakar un kaamyab bacho ke sirf "name" nikal lein.
# End mein topper bacho ke naamon ki saaf suthri list dikhaein.
students = [
    {"name": "Babar", "gpa": 3.8},
    {"name": "Zeeshan", "gpa": 2.4},
    {"name": "Arshma", "gpa": 3.9}
]
filter_students = list (filter (lambda x : x["gpa"] > 3.5, students) )
print("Filter students = " , filter_students)
map_st = list( map (lambda x: x["name"], filter_students))
print("Map students = " , map_st)