# =====================================================================
# TOPIC: PYTHON CLASSES AND OBJECTS (OOP Basics, __init__, Methods, self)
# TOTAL QUESTIONS: 6 (1 Easy, 2 Medium, 3 Hard)
# INSTRUCTIONS: Write your Python code below each comment block.
# =====================================================================

# ---------------------------------------------------------------------
# 🟢 EASY LEVEL
# ---------------------------------------------------------------------

# QUESTION 1: University Student Card Blueprint
# `class` keyword ka use kar ke `Student` naam ka ek naqsha banayein.
# Is class mein ek aam method (function) banayein: `say_hello(self)`.
# Yeh method screen par print kare: "Assalam-o-Alaikum UOG Students! 🎓".
# Baahir aa kar is class ka ek object banayein aur function call karein.
class Student():
    def say_hello(self):
        print("Assalam-o-Alaikum UOG Students!")
s = Student()
s.say_hello()

# ---------------------------------------------------------------------
# 🟡 MEDIUM LEVEL
# ---------------------------------------------------------------------

# QUESTION 2: Mobile Phone Factory (__init__ Constructor)
# Ek class banayein `Mobile`. Isme jadui `__init__(self, brand, battery)`
# function lagayein jo object bante hi brand aur battery save kare.
# Ek method banayein `show_details(self)` jo screen par dikhaye:
# "Yeh [brand] ka phone hai aur iski battery [battery]% hai."
# Baahir do alag alag phones (objects) bana kar details check karein.
class Mobile():
    def __init__(self,brand,battery):
        self.brand = brand
        self.battery = battery
    def show_details(self):
        print(f"Yeh {self.brand} ka phone hai aur iski battery {self.battery}{"%"} hai.")
m1 = Mobile("Samsung",70)
m1.show_details()
m2 = Mobile("Oppo",98)
m2.show_details()

# QUESTION 3: Safe Bank Wallet (Modifying Attributes)
# Ek class banayein `BankWallet`. Constructor `__init__` ke andar
# user ka naam lein aur shuruati balance automatic 0.0 rakh dein (balance=0.0).
# Ek method banayein `deposit(self, amount)` jo balance mein paise plus kare.
# Baahir ek object banayein, pehle check karein balance kya hai,
# phir 500 rupees deposit kar ke naya balance print karein.
class BankWallet():
    def __init__(self,name,balance = 0.0):
        self.name = name
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
bank = BankWallet("Babar")
print("Intial balance = " , bank.balance)
bank.deposit(500)
print("After adding 500 , balance = ", bank.balance)

# ---------------------------------------------------------------------
# 🔴 HARD LEVEL
# ---------------------------------------------------------------------

# QUESTION 4: Smart Fitness Tracker (State Management)
# Ek advanced class banayein `FitnessTracker`. Shuru mein steps = 0 rakhein.
# Is class mein teen alag alag methods hone chahiye:
# 1. `walk(self)` -> Jab ye chale, steps mein 1000 jama ho jayein.
# 2. `run(self)` -> Jab ye chale, steps mein 3000 jama ho jayein.
# 3. `reset(self)` -> Yeh steps ko dobara 0 kar de.
# Baahir object bana kar thoda chalaein aur steps ki ginti check karein.
class FitnessTracker():
    steps = 0
    def walk(self):
        self.steps += 1000
    def run(self):
        self.steps += 3000
    def reset(self):
        self.steps = 0
f = FitnessTracker()
print("Intial steps = " , f.steps)
f.walk()
print("After walk , steps = " , f.steps)
f.run()
print("After running, steps = " , f.steps)
f.reset()
print("After reset, steps = " , f.steps)

# QUESTION 5: Supermarket Product Discount (Methods with Parameters)
# Ek class banayein `Product` jisme name aur price constructor mein aayein.
# Is class ke andar ek method banayein: `apply_discount(self, percentage)`.
# Yeh method price par diya hua percentage discount cut karega
# aur bachi hui discounted price ko `return` karega.
# Testing: "Laptop" keemat 50000 par 10% discount chalakar check karein.
class Product():
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def apply_discount(self, percentage):
        p = percentage / 100 
        res = p * self.price
        return self.price - res
laptop = Product("laptop",50000)
print("Price after discount = ",laptop.apply_discount(10))

# QUESTION 6: University Project Group Manager (List inside Class)
# Ek class banayein `ProjectGroup` jisme group ka name constructor mein aaye.
# Is class ke andar automatic ek khali list banayein: `self.members = []`.
# Do methods banayein:
# 1. `add_member(self, name)` -> Jo list mein naya naam append kare.
# 2. `show_group(self)` -> Jo loop chalakar saare members ke naam dikhaye.
# Apne group ke liye object bana kar 3 dosto ke naam add kar ke dikhaein.
class ProjectGroup():
    def __init__(self,name):
        self.name = name
        self.members = []
    def add_member(self, names):
        self.members.append(names)
    def show_group(self):
        for m in self.members:
            print("Member name = " , m)
df = ProjectGroup("Deadline Fighters")
df.add_member("Babar")
df.add_member("ALi")
df.add_member("Zeeshan")
df.show_group()