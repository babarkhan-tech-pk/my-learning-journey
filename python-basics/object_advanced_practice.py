# =====================================================================
# TOPIC: PYTHON OBJECTS (Instantiation, Identity, Interaction & Lists)
# TOTAL QUESTIONS: 6 (1 Easy, 2 Medium, 3 Hard)
# INSTRUCTIONS: Write your Python code below each comment block.
# =====================================================================

# PRE-DEFINED CLASSES FOR YOUR ASSIGNMENTS (Do not change these)
class ATMCard:
    def __init__(self, owner): self.owner = owner

class Ticket:
    def __init__(self, movie): self.movie = movie

class DeliveryDriver:
    def __init__(self, name): self.name = name

class GymMember:
    def __init__(self, name, status):
        self.name = name
        self.status = status # "Active" ya "Inactive"

class Car:
    def __init__(self, model):
        self.model = model
        self.fuel_tank = "Empty"

class PetrolPump:
    def fill_car(self, car_object):
        car_object.fuel_tank = "Full"

# ---------------------------------------------------------------------
# 🟢 EASY LEVEL
# ---------------------------------------------------------------------

# QUESTION 1: The ATM Card Object Creation
# Oopar bani hui `ATMCard` class ka use karein.
# "Babar" naam ke owner ke sath ek asli object banayein.
# Python ke built-in type() function ka use kar ke screen
# par check karein ke is object ki asli shakal (type) kya hai.
class ATMCard:
    def __init__(self, owner): self.owner = owner
atm = ATMCard("Babar")
print("Class type = " , type(ATMCard))
print("Object type = " , type(atm))

# ---------------------------------------------------------------------
# 🟡 MEDIUM LEVEL
# ---------------------------------------------------------------------

# QUESTION 2: Twin Cinema Tickets (Object Identity)
# Oopar bani hui `Ticket` class ka use karein.
# Do alag alag objects banayein: t1 aur t2, dono mein movie "Maula Jatt" rakhein.
# 1. `==` operator se check karein ke kya dono ka andar ka data same hai.
# 2. `is` operator se check karein ke kya computer ki memory mein ye dono 
# ek hi asli object hain ya alag alag. Dono ka jawab print karein.
class Ticket:
    def __init__(self, movie): self.movie = movie
t1 = Ticket("Maula Jatt")
t2 = Ticket("Maula Jatt")
print("Dono Name same ya nahi : " , t1.movie == t2.movie)
print(id(t1))
print(id(t2))

# QUESTION 3: Dynamic Badge on Delivery Driver
# Oopar bani hui `DeliveryDriver` class se ek object banayein: driver1.
# Driver ka naam rakhein "Zeeshan". Python mein hum class ke bahar se 
# bhi kisi object mein naya attribute (variable) jor sakte hain!
# Object banay ke baad, line ke bahar se `driver1.rating = 4.8` likhein.
# Phir driver ka naam aur uski rating dono screen par print karein.
class DeliveryDriver:
    def __init__(self, name): self.name = name
driver1 = DeliveryDriver("Zeeshan")
driver1.rating = 4.8
print("Driver name = " , driver1.name)
print("Driver rating = " , driver1.rating)

# ---------------------------------------------------------------------
# 🔴 HARD LEVEL
# ---------------------------------------------------------------------

# QUESTION 4: Gym Attendance Scanner (List of Objects)
# Oopar bani hui `GymMember` class ka use karte hue 3 members ke objects banayein:
# m1 ("Babar", "Active"), m2 ("Ali", "Inactive"), m3 ("Arshma", "Active").
# In teeno objects ko ek list mein band karein: members_list = [m1, m2, m3]
# For loop chalayein jo is list ke andar jaye, aur sirf un bacho ka
# naam print kare jin ka status exactly "Active" hai.
class GymMember:
    def __init__(self, name, status):
        self.name = name
        self.status = status # "Active" ya "Inactive"
m1 = GymMember("Babar", "Active")
m2 = GymMember("Ali", "Inactive")
m3 = GymMember("Arshma", "Active")
members_list = [m1, m2, m3]
for m in members_list:
    if m.status == "Active":
        print("Member name = " , m.name)

# QUESTION 5: Car Refueling Station (Object Interaction)
# Oopar mojud `Car` aur `PetrolPump` dono classes ka use karein.
# 1. Car class se ek object banayein: `my_car = Car("Civic")`.
# 2. PetrolPump class se ek object banayein: `pump = PetrolPump()`.
# 3. Pehle car ka fuel_tank print karein (jo shuru mein Empty hoga).
# 4. Phir pump ke `fill_car()` method ko chalaein aur parameter mein 
# poora ka poora `my_car` object bhej dein! Car ka naya fuel_tank dikhaein.
class Car:
    def __init__(self, model):
        self.model = model
        self.fuel_tank = "Empty"

class PetrolPump:
    def fill_car(self, car_object):
        car_object.fuel_tank = "Full"
my_car = Car("Civic")
pump = PetrolPump()
print("Fuel tank = " , my_car.fuel_tank)
pump.fill_car(my_car)
print("Fuel tank now = " , my_car.fuel_tank)

# QUESTION 6: Netflix Profile Sharing (Reference vs Copy)
# `ATMCard` class ka use kar ke ek profile banayein: `profile1 = ATMCard("Khan")`.
# Ab ek naya variable banayein: `profile2 = profile1` (Reference Assignment).
# Python ke built-in `id()` function ka use kar ke dono profiles ki
# khufia memory location (ID) screen par print karein.
# Comment mein batayein ke kya dono aik hi tijori ko ishara kar rahe hain?
class ATMCard:
    def __init__(self, owner): self.owner = owner
profile1 = ATMCard("Khan")
profile2 = profile1
print("Profile 1 ki memory location = " , id(profile1))
print("Profile 2 ki memory location = " , id(profile2))