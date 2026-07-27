# =====================================================================
# TOPIC: VARIABLE SCOPE (Global/Local), *args AND **kwargs IN PYTHON
# TOTAL QUESTIONS: 6 (1 Easy, 2 Medium, 3 Hard)
# INSTRUCTIONS: Write your Python code below each comment block.
# =====================================================================

# ---------------------------------------------------------------------
# 🟢 EASY LEVEL
# ---------------------------------------------------------------------

# QUESTION 1: Ghar ka Chula vs Shehar ki Sarak (Global vs Local)
# Ek global variable banayein: `city_light = "Yellow"`
# Ab ek function banayein: `house_room()`
# Function ke andar ek local variable banayein: `room_bulb = "White"`
# Function ke andar dono variables ko print karne ki koshish karein.
# Function ke baahir aa kar check karein ke kya `room_bulb` 
# print hota hai ya computer darr kar error deta hai!
city_light = "Yellow"
def house_room():
    room_bulb = "White"
    print("City light = " , city_light)
    print("House room light = " , room_bulb)
house_room()
print("City light = " , city_light)
# print("House room light = " , room_bulb)

# ---------------------------------------------------------------------
# 🟡 MEDIUM LEVEL
# ---------------------------------------------------------------------

# QUESTION 2: Unlimited Cricket Match Scores (*args)
# Aap ek cricket match ke liye score counter bana rahe hain.
# Hamein nahi pata ke batsmen agli kitni balls par kitne runs banaye ga.
# `def total_score(*args)` naam ka ek function banayein.
# Yeh function jitne bhi numbers parameter mein diye jayein (unlimited),
# loop chalakar un sab ko plus kare aur total score return kare.
# Is machine ko testing ke liye 4, 6, 1, 2, 6 runs de kar chalaein.
def total_score(*args):
    sum = 0
    for x in args:
        sum += x
    return sum
print("Test 1 = " , total_score(4,6,1,2,6))
print("Test 2 = " , total_score(461,681,199))

# QUESTION 3: Wallet Money Updater (The global Keyword)
# Aapke pass ek global variable hai: `wallet_balance = 500`
# Ek function banayein: `add_money(amount)`
# Is function ke andar global balance mein naye paise plus karne hain.
# Yaad rakhein, bina `global` keyword ke computer variable change 
# nahi karne dega! Balance update kar ke final amount dikhaein.
wallet_balance = 500
def add_money(amount):
    global wallet_balance
    print("Before Adding amount : ", wallet_balance)
    wallet_balance += amount
    print("After Adding amount : ", wallet_balance)
add_money(0)
add_money(78987)
add_money(789.09)

# ---------------------------------------------------------------------
# 🔴 HARD LEVEL
# ---------------------------------------------------------------------

# QUESTION 4: Dynamic Student Bio Data (**kwargs)
# University group ke bacho ka data save karne ke liye machine banayein:
# `def save_student_profile(**kwargs)`
# Yeh machine unlimited key-value pairs le sakti hai.
# Function ke andar `.items()` ka loop chalayein aur saaf suthra print 
# karein ke kaunsi Key mein kya Value mojud hai.
# Testing ke liye name="Arshma", role="Developer", status="Active" dein.
def save_student_profile(**kwargs):
    for k,v in kwargs.items():
        print(k, " = " , v)
save_student_profile(name="Ahsan", role="Developer", status="Active")
save_student_profile(name="Babar", role="Admin", status="In Active")

# QUESTION 5: Grand Royal Biryani Order (Combining *args and **kwargs)
# Ek hotel app ke liye function banayein: `make_biryani_order(size, *extras, **details)`
# 1. Size aam variable hoga (e.g., "Large").
# 2. *extras mein unlimited toppings aayengi (e.g., "Raita", "Salad", "Shami").
# 3. **details mein delivery ka pata wagera hoga (e.g., table=5, vip=True).
# Teeno ko function ke andar alag alag khoobsurat tareeqay se print karein.
def make_biryani_order(size, *extras, **details):
    print("SIze = ", size)
    for x in extras:
        print("Item = " , x)
    for k,v in details.items():
        print(k, " = " , v)
make_biryani_order("Large",("Raita", "Salad", "Shami"),{"table":5, "vip":True})

# QUESTION 6: Smart Counter Token Tracker (Enclosing Scope & global)
# Ek global counter variable banayein: `token_id = 1000`
# Ek main function banayein: `issue_ticket()`
# Uske andar `global` keyword ka use kar ke `token_id` ko + 1 karein.
# Phir `issue_ticket` ke andar hi ek aur chota function (Inner function)
# banayein jo bache ka naam lekar ticket aur token dono print kare.
# Outer function ke end mein inner function ko call karna mat bhooliyega!
token_id = 1000
def issue_ticket():
    global token_id
    token_id += 1
    def inner_function(name):
        print("Name = ", name)
        print("Token Id = " , token_id)
    inner_function("Ali")
    inner_function("Ahmed")
issue_ticket()