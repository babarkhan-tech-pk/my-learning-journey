# =====================================================================
# TOPIC: METHOD OVERRIDING IN PYTHON (Inheritance, super() Keyword)
# TOTAL QUESTIONS: 6 (1 Easy, 2 Medium, 3 Hard)
# INSTRUCTIONS: Write your Python code below each comment block.
# =====================================================================

# ---------------------------------------------------------------------
# 🟢 EASY LEVEL
# ---------------------------------------------------------------------

# QUESTION 1: The Animal Sound Changer
# Ek parent class banayein `Animal` jisme ek method ho: `make_sound()`.
# Yeh method screen par print kare: "Animal makes a generic sound".
# Ab ek child class banayein `Cat` jo Animal se inherit kare.
# Cat ke andar `make_sound()` ko override (dobara likhein) karein
# taake wo sirf "Meow! 🐱" print kare. Baahir object bana kar chalayein.
class Animal():
    def make_sound(self):
        print("Animal makes a generic sound")
class Cat(Animal):
    def make_sound(self):
        print("Meow")
a = Animal()
a.make_sound()
c = Cat()
c.make_sound()

# ---------------------------------------------------------------------
# 🟡 MEDIUM LEVEL
# ---------------------------------------------------------------------

# QUESTION 2: University Student Portal Update
# Parent class banayein `UOGStudent` jisme method ho `open_portal()`.
# Yeh method print kare: "Welcome to Basic Student Portal."
# Child class banayein `DataScienceStudent`. Isme `open_portal()` ko 
# override karein taake jab data science ka bacha portal khole to print ho:
# "Welcome to Advanced AI & Data Science Portal! 🚀"
class UOGStudent():
    def open_portal(self):
        print("Welcome to Basic Student Portal.")
class DataScienceStudent():
    def open_portal(self):
        print("Welcome to Advanced AI & Data Science Portal!")
u = UOGStudent()
u.open_portal()
d = DataScienceStudent()
d.open_portal()

# QUESTION 3: The VIP No-Fee Wallet
# Parent class banayein `BasicWallet`. Isme method ho `send_money(amount)`.
# Yeh method total bill mein 50 rupees fee plus kar ke print kare:
# "Sent [amount]. Fee charged: 50. Total: [amount + 50]".
# Child class banayein `VIPWallet` aur `send_money` ko override karein.
# VIP user ke liye koi fee nahi hogi, direct "Sent [amount] with 0 fee!" print ho.
class BasicWallet():
    def send_money(self,amount):
        print(f"Sent {amount}. Fee charged: 50. Total: [{amount + 50}]")
class VIPWallet():
    def send_money(self,amount):
        print(f"Sent {amount} with 0 fee!")
b = BasicWallet()
b.send_money(1000)
v = VIPWallet()
v.send_money(1000)

# ---------------------------------------------------------------------
# 🔴 HARD LEVEL
# ---------------------------------------------------------------------

# QUESTION 4: Bank Account Bonus Interest (Using super())
# Parent class banayein `BankAccount`. Isme method ho `get_interest(balance)`.
# Yeh method 5% interest return kare (balance * 0.05).
# Child class banayein `SavingsAccount` aur is method ko override karein.
# Savings account mein abba wala interest bhi milega AUR 200 rupees extra bonus!
# Inside child method, `super()` ka use kar ke abba wala interest nikalen,
# usme 200 plus kar ke final jawab return karein.
class BankAccount():
    def get_interest(self, balance):
        return balance * 0.05
class SavingsAccount(BankAccount):
    def get_interest(self , balance):
        b = super().get_interest(balance) 
        res = b + 200
        return res
b = BankAccount()
print(b.get_interest(5000))
s = SavingsAccount()
print(s.get_interest(5000))

# QUESTION 5: Sports Car Safety Mode (Conditional Overriding)
# Parent class banayein `Vehicle` jisme method ho `accelerate()`.
# Yeh method screen par print kare: "Speed is 60 km/h."
# Child class banayein `SportsCar` jisme variable ho `self.safety_mode = True`.
# `accelerate()` ko override karein: Agar safety_mode True hai, to `super()`
# ka use kar ke abba wali normal speed (60) hi chalayein.
# Agar safety_mode False ho, to print karein: "Speed is 150 km/h! 🏎️".
class Vehicle():
    def accelerate(self):
        print("Speed is 60 km/h.")
class SportsCar(Vehicle):
    def __init__(self):
        self.safety_mode = False
    def accelerate(self):
        if self.safety_mode == True:
            super().accelerate()
        else:
            print("Speed is 150 km/h.")
v = Vehicle()
v.accelerate()
sc = SportsCar()
sc.accelerate()

# QUESTION 6: University Group Payroll (Polymorphism Loop)
# Parent class banayein `Employee` jisme method ho `get_salary()` (returns 30000).
# Child class 1 banayein `Manager` jo salary override kar ke 80000 return kare.
# Child class 2 banayein `Intern` jo salary override kar ke 15000 return kare.
# Baahir teeno classes ka ek ek object banayein aur unhein ek list mein dalein.
# For loop chalakar har object ka `get_salary()` call karein (Polymorphic loop).
class Employee():
    def get_salary(self):
        return 30000
class Manager(Employee):
    def get_salary(delf):
        return 80000
class Intern(Employee):
    def get_salary(self):
        return 15000
e = Employee()
m = Manager()
i = Intern()
li = [e,m,i]
for i in li:
    print(i.get_salary())