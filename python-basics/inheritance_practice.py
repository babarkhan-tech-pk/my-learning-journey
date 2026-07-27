# =====================================================================
# TOPIC: PYTHON INHERITANCE (Single, Multi-level, Multiple & super())
# TOTAL QUESTIONS: 6 (1 Easy, 2 Medium, 3 Hard)
# INSTRUCTIONS: Write your Python code below each comment block.
# =====================================================================

# ---------------------------------------------------------------------
# 🟢 EASY LEVEL
# ---------------------------------------------------------------------

# QUESTION 1: The Basic Electronic Device (Single Inheritance)
# Ek parent class banayein `Device` jisme brand name constructor mein aaye.
# Isme ek method banayein `turn_on(self)` jo "Device is now ON" print kare.
# Ab ek child class banayein `SmartPhone` jo `Device` se inherit kare.
# Smartphone ke andar koi naya function likhne ki zaroorat nahi hai.
# Baahir Smartphone ka object banayein aur abba wala `turn_on` chalayein.
class Device():
    def __init__(self , brand):
        self.brand = brand
    def turn_on(self):
        print(self.brand," , Brand Device is turning on..")
class SmartPhone(Device):
    pass
#d = Device("Samsung")
sm = SmartPhone("Hawai")
sm.turn_on()

# ---------------------------------------------------------------------
# 🟡 MEDIUM LEVEL
# ---------------------------------------------------------------------

# QUESTION 2: University Multi-Level Hierarchy (Multi-Level Inheritance)
# 1. Sab se oopar ek dada class banayein `Person` (jisme name constructor mein aaye).
# 2. Phir ek abba class banayein `UOGStudent` jo `Person` se li gayi ho.
# 3. Phir ek beta class banayein `DataSciStudent` jo `UOGStudent` se li gayi ho.
# DataSciStudent ke andar ek method banayein `show_major(self)` jo dikhaye:
# "[name] ka major Data Science hai 📊".
# Beta class ka object bana kar check karein ke kya dada ka naam chalta hai.
class Person():
    def __init__(self , name):
        self.name = name
class UOGStudent(Person):
    print("I am a UOG student.")
class DataSciStudent(UOGStudent):
    def show_major(self):
        print(self.name , " , ka major Data science hay.")
# p = Person("Babar")
# uogs = UOGStudent()
dss = DataSciStudent("Babar")
dss.show_major()

# QUESTION 3: Garage Vehicle Share (Hierarchical Inheritance)
# Ek parent class banayein `Vehicle` jisme method ho `horn(self)` -> "Pee Peee!".
# Ab do alag alag child classes banayein: `Car` aur `Bike`.
# Ghaur se dekhein, dono classes ek hi parent `Vehicle` se juri honi chahiye.
# Baahir Car ka bhi object banayein aur Bike ka bhi object banayein.
# Check karein ke kya dono alag alag objects abba ka horn baja sakte hain?
class Vehicle():
    def horn(self):
        print("Pee pee..")
class Car(Vehicle):
    pass
class Bike(Vehicle):
    pass
v = Vehicle()
c = Car()
b = Bike()
v.horn()
c.horn()
b.horn()

# ---------------------------------------------------------------------
# 🔴 HARD LEVEL
# ---------------------------------------------------------------------

# QUESTION 4: The Full-Stack Student (Multiple Inheritance)
# Python mein ek bacha do alag alag classes se bhi warsa le sakta hai!
# 1. Pehli class banayein `CodingSkills` jisme method ho `write_python()`.
# 2. Doosri class banayein `DesignSkills` jisme method ho `design_ui()`.
# 3. Teesri child class banayein `FullStackStudent` jo DONO classes se 
#    ek sath inherit kare (class FullStackStudent(CodingSkills, DesignSkills):)
# Baahir child ka object bana kar dono abba-amma ke functions chalayein.
class CodingSkills():
    def write_python(self):
        print("Mujhy python ati hay.")
class DesignSkills():
    def design_ui(self):
        print("I have learned Design UI.")
class FullStackStudent(CodingSkills,DesignSkills):
    pass
fss = FullStackStudent()
fss.write_python()
fss.design_ui()

# QUESTION 5: Secure Database User Passport (super() with __init__)
# Parent class banayein `User` jisme constructor `__init__` ke andar `username` aaye.
# Child class banayein `Admin`. Admin ke paas apna ek naya variable bhi hai: `secret_key`.
# Admin ka constructor banate waqt `super().__init__(username)` ka use karein
# taake username automatic abba class wale system mein chala jaye, aur
# `self.secret_key` ko child mein save karein. Details print kar ke dikhaein.
class User():
    def __init__(self,user_name):
        self.user_name = user_name
class Admin(User):
    def __init__(self,secret_key):
        super()
        self.secret_key = secret_key
u = User("Babar")
a = Admin("567")
print(u.user_name , " , " , a.secret_key)

# QUESTION 6: Smart Home Power Manager (Method Resolution Order - MRO)
# Do parent classes banayein: `SolarPower` (method: `get_source()` -> "Sun ☀️")
# aur `WapdaPower` (method: `get_source()` -> "Grid ⚡").
# Child class banayein `SmartHouse` jo dono se inherit kare.
# Pehle `SolarPower` likhein phir `WapdaPower` inheritance ke bracket mein.
# Baahir object bana kar `get_source()` chalayein aur comment mein batayein
# ke computer ne pehle kis parent ki baat suni aur kyun!
class SolarPower():
    def get_source(self):
        print("Sun")
class WapdaPower():
    def get_source(self):
        print("Grid")
class SmartHouse(SolarPower,WapdaPower):
    pass
sh = SmartHouse()
sh.get_source()