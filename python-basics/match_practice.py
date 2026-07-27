# =====================================================================
# TOPIC: MATCH-CASE KEYWORD IN PYTHON (Structural Pattern Matching)
# TOTAL QUESTIONS: 6 (1 Easy, 2 Medium, 3 Hard)
# INSTRUCTIONS: Write your Python code below each comment block.
# =====================================================================

# ---------------------------------------------------------------------
# 🟢 EASY LEVEL
# ---------------------------------------------------------------------

# QUESTION 1: Simple Discount Voucher
# Aap ek grocery store ke liye billing system bana rahe hain.
# User se voucher code input lein (e.g., "SAVE10", "SAVE20").
# Match-case ka istemal kar ke print karein ke kitna discount mila.
# Agar code "SAVE10" ho to "10% Discount", agar "SAVE20" ho to 
# "20% Discount", aur agar koi aur faltoo code ho to print karein:
# "Invalid Voucher Code! ❌".
user = input("Enter your voucher code : ")
user = user.lower()
match user:
    case 'save10':
        print("You have saved 10%.")
    case 'save20':
        print("You have saved 20%.")
    case _:
        print("Invalid Voucher code.")

# ---------------------------------------------------------------------
# 🟡 MEDIUM LEVEL
# ---------------------------------------------------------------------

# QUESTION 2: Weekend or Weekday Checker
# User se hafte ke kisi ek din ka naam input lein (e.g., "Monday").
# Match-case mein Pipe Operator (|) ka istemal karein.
# Agar input Monday se Friday ke darmiyan ho, to aik hi case mein 
# print karein: "Chalo kaam par chalo! 👔".
# Agar Saturday ya Sunday ho, to print karein: "Mubarak ho, Weekend hai! 🎉".
# Agar spelling galat ho to print karein: "Galt din ka naam likha hai!".
day = input("Enter a day of week? ")
day = day.lower()
match day:
    case 'monday' | 'tuesday' | 'wedensday' | 'thursday' | 'friday':
        print("Chalo kaam par chalo!")
    case 'saturday' | 'sunday':
        print("Mubarak ho, Weekend hai!")
    case _:
        print("Galt din ka naam likha hai!")

# QUESTION 3: Fast-Food Size Selector
# Ek pizza shop par customer size choose karta hai.
# User se pizza size input lein (e.g., "S", "Small", "M", "Medium").
# Match-case ke zariye handles karein:
# Agar user "S" YA "Small" likhe (Pipe operator use karein) to keemat 500 batayein.
# Agar "M" YA "Medium" likhe to keemat 1000 batayein.
# Agar "L" YA "Large" likhe to keemat 1500 batayein.
# Baqi tamam suraton mein "Size available nahi hai" print karein.
size = input("Enter pizza size (S : small / M : medium / L : large) ")
size = size.lower()
match size:
    case 's':
        print("Price = 500")
    case 'm':
        print("Price = 1000")
    case 'l':
        print("Price = 1500")
    case _:
        print("Size available nahi hai")

# ---------------------------------------------------------------------
# 🔴 HARD LEVEL
# ---------------------------------------------------------------------

# QUESTION 4: Robot Remote Control (List/Pattern Matching)
# Ek robot command sunta hai. User se do alfaz ka input lein.
# Input ko split() kar ke ek list banayein (e.g., ["MOVE", "UP"]).
# Match-case ka istemal kar ke check karein:
# Agar list ["MOVE", "UP"] ho to print karein: "Robot upar ja raha hai".
# Agar list ["MOVE", "DOWN"] ho to print karein: "Robot neeche ja raha hai".
# Agar pehla lafz "STOP" ho aur doosra kuch bhi ho (case ["STOP", _]), 
# to print karein: "Robot ruk gaya!". Warna: "Command samajh nahi aayi".
command = input("Command enter karen? ")
cmd_list = command.split()
match cmd_list:
    case ["MOVE","UP"]:
        print("Robot uper ja rha hay.")
    case ["MOVE","DOWN"]:
        print("Robot nechy ja rha hay.")
    case ["STOP", _]:
        print("Robot ruk rha hay..")
    case _:
        print("Command smaj nai ayi.")

# QUESTION 5: Smart Login Verification (Tuple Matching)
# Ek khufia database mein user ka status ek Tuple mein band hai.
# Farz karein aik variable hai: user_status = ("Admin", True)
# Pehla hissa Role hai, aur doosra hissa Verification state (True/False) hai.
# Match-case se is Tuple ko scan karein:
# Case 1: Agar ("Admin", True) ho to "Full Dashboard Open 🔓" print karein.
# Case 2: Agar ("Admin", False) ho to "Please verify your Admin account!" print karein.
# Case 3: Agar Role "User" ho aur verified True ho, to "User Profile Open" print karein.
# Default case (_) mein print karein: "Access Denied! ❌".
user_status = ("User", False)
match user_status:
    case ("Admin", True):
        print("Full Dashboard Open")
    case ("Admin", False):
        print("Please verify your Admin account!")
    case ("User", True):
        print("User Profile Open")
    case _:
        print("Access Denied!")

# QUESTION 6: E-Commerce Price Guard (Matching with If-Condition)
# Aap ek online shop par products check kar rahe hain.
# Ek list bani hui hai jis mein product ka naam aur price hai: item = ["Mobile", 15000]
# Match-case ka istemal kar ke list ko unpack karein: case [name, price]:
# Is case ke sath IF condition (Guard) lagayein:
# Agar price 10000 se zyada hai, to print karein: "[name] boht mehanga hai!".
# Agar price 10000 ya us se kam hai, to print karein: "[name] munasib keemat mein hai."
# Yaad rakhein, yahan case ke andar hi IF guard use karna hai!
item = ["Mobile", 9000]
match item:
    case [name,price] if price > 10000:
        print(name," Boht mehnga hay.")
    case [name,price]:
        print(name, " Munasib qeemat hay.")
    case _:
        print("Gahalt input.")