# =====================================================================
# TOPIC: PYTHON ABSTRACTION (ABC, @abstractmethod, Interface Enforcing)
# TOTAL QUESTIONS: 6 (1 Easy, 2 Medium, 3 Hard)
# INSTRUCTIONS: Write your Python code below each comment block.
# =====================================================================

# Sab se pehle abstraction ke jadui auzaar import karein
from abc import ABC, abstractmethod

# ---------------------------------------------------------------------
# 🟢 EASY LEVEL
# ---------------------------------------------------------------------

# QUESTION 1: The Standard Vehicle Template
# Ek abstract base class banayein `Vehicle` jo ABC se inherit kare.
# Iske andar `@abstractmethod` lagakar `start_engine(self)` banayein.
# Yaad rakhein, abstract method ke andar sirf `pass` likha jata hai.
# Ab ek child class banayein `Car`. Car ke andar is method ko 
# lazmi override karein aur print karein: "Car engine started! 🚗".
# Baahir Car ka object bana kar chalaein.
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started.")
c = Car()
c.start_engine()

# ---------------------------------------------------------------------
# 🟡 MEDIUM LEVEL
# ---------------------------------------------------------------------

# QUESTION 2: Universal TV Remote (Interface Enforcing)
# Ek abstract class banayein `TVRemote` (ABC use karein).
# Isme ek abstract method rakhein: `press_power_button(self)`.
# Ab ek child class banayein `SonyRemote`. 
# Agar SonyRemote is method ko override nahi karegi to error aaye ga!
# SonyRemote mein isay implement karein aur "Sony TV Turned ON 📺" print karein.
from abc import ABC, abstractmethod
class TVRemote(ABC):
    @abstractmethod
    def press_power_button(self):
        pass
class SonyRemote(TVRemote):
    def press_power_button(self):
        print("Sony TV Turned ON")
sr = SonyRemote()
sr.press_power_button()

# QUESTION 3: Secure Mobile Payment Gateway
# Ek abstract class banayein `PaymentGateway`.
# Isme abstract method banayein `process_payment(self, amount)`.
# Child class banayein `EasyPaisa`. EasyPaisa ke andar is function ko 
# open karein aur print karein: "[amount] Rupees transferred via EasyPaisa! 💸".
# Baahir 1500 ka transaction kar ke check karein.
from abc import ABC, abstractmethod
class PaymentGateway(ABC):
    @abstractmethod 
    def process_payment(self, amount):
        pass
class EasyPaisa(PaymentGateway):
    def process_payment(self, amount):
        print(amount , " Rupees transferred via EasyPaisa!")
ep = EasyPaisa()
ep.process_payment(150)

# ---------------------------------------------------------------------
# 🔴 HARD LEVEL
# ---------------------------------------------------------------------

# QUESTION 4: The Un-instantiable Law (Abstract Class Object Error)
# Abstraction ka rule hai ke abstract class ka direct object nahi ban sakta.
# Ek abstract class banayein `UOGExam` jisme abstract method ho `show_date()`.
# Child class banayein `DataScienceExam` aur usme method implement karein.
# Baahir aa kar jaan boojh kar pehle parent class ka object banane ki koshish 
# karein: `test = UOGExam()` aur try-except se TypeError pakar kar dikhaein!
from abc import ABC, abstractmethod
class UOGExam(ABC):
    @abstractmethod
    def show_date(self):
        pass
class DSExam(UOGExam):
    def show_date(self):
        print("Date is Not decided yet.")
# uoge = UOGExam()
#uoge.show_date()
dse = DSExam()
dse.show_date()

# QUESTION 5: Smart Appliance Box (Mixed Normal & Abstract Methods)
# Ek abstract class mein normal functions bhi ho sakte hain!
# Abstract class banayein `Appliance` jisme:
# 1. Ek aam method ho `turn_on(self)` jo "Power is ON" print kare.
# 2. Ek abstract method ho `do_work(self)` jis par thappa laga ho.
# Child class banayein `AirConditioner`. Isme `do_work()` ko implement kar ke 
# "Cooling started! ❄️" print karein. Child ka object bana kar dono functions chalaein.
from abc import ABC, abstractmethod
class Appliance(ABC):
    def turn_on(self):
        print("Appliance turnign on..")
    @abstractmethod
    def do_work(self):
        pass
class AC(Appliance):
    def do_work(self):
        print("Cooling started..")
ac = AC()
ac.turn_on()
ac.do_work()

# QUESTION 6: Strict Database CRUD Rulebook (Multiple Abstract Methods)
# Ek abstract class banayein `DatabaseConnection`.
# Is baar aapne DO laws (abstract methods) lagane hain:
# 1. `connect(self)` 
# 2. `disconnect(self)`
# Child class banayein `SQLServer2022`. SQL Server ko dono functions lazmi 
# implement karne parenge, agar ek bhi chora to Python chalne nahi dega!
# Dono functions mein simple print messages likh kar test karein.
from abc import ABC, abstractmethod
class DBC(ABC):
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def dis_connect(self):
        pass
class SQLS(DBC):
    def connect(self):
        print("DB Connected..")
    def dis_connect(self):
        print("DB not connected..")
sql = SQLS()
sql.connect()
sql.dis_connect()