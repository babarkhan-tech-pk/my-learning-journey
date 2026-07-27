# =====================================================================
# TOPIC: PYTHON ENCAPSULATION (Private/Protected Attributes, Getters & Setters)
# TOTAL QUESTIONS: 6 (1 Easy, 2 Medium, 3 Hard)
# INSTRUCTIONS: Write your Python code below each comment block.
# =====================================================================

# ---------------------------------------------------------------------
# 🟢 EASY LEVEL
# ---------------------------------------------------------------------

# QUESTION 1: Secret ATM PIN Locker
# `class` keyword ka use kar ke `AtmCard` naam ki class banayein.
# Constructor mein user ka name aur ek private PIN code rakhein.
# Yaad rakhein, private karne ke liye `self.__pin` likhna hoga.
# Ek public method `show_pin(self)` banayein jo PIN print kare.
# Baahir object bana kar check karein ke kya direct PIN print hota hai 
# ya sirf function ke zariye hi bahaar aata hai.
class ATMCard():
    def __init__(self,name,pin):
        self.name = name
        self.__pin = pin
    def print_pin(self):
        print("Pin = " , self.__pin)
atm = ATMCard("Babar","89FR6y")
atm.print_pin()

# ---------------------------------------------------------------------
# 🟡 MEDIUM LEVEL
# ---------------------------------------------------------------------

# QUESTION 2: Smart Laptop Password Guard (Setter with Validation)
# Ek class banayein `Laptop` jisme ek private variable ho `self.__password`.
# Is class ke andar ek setter method banayein: `change_password(self, new_pass)`.
# Yeh setter pehle IF condition se check kare ke agar naye password ki 
# lambai (length) 4 characters se kam hai, to error message de.
# Agar password 4 ya us se bada hai, to hi private variable ko update kare.
# Baahir object bana kar dono suraton ko test karein.
class Laptop():
    def __init__(self , password):
        self.__password = password
    def change_pass(self,new_pass):
        if len(new_pass) >= 4:
            print("Old Password = " , self.__password)
            self.__password = new_pass
            print("New password = " , self.__password)
        else:
            print("Passeord 4 ya zyada characters ka ho.")
lt = Laptop("567895")
lt.change_pass("56790")
lt.change_pass("456")

# QUESTION 3: Room Thermostat Controller (Getter and Setter)
# Ek class banayein `Thermostat` jisme private variable ho `self.__temp = 22`.
# Do alag alag methods banayein:
# 1. `get_temperature(self)` -> Jo current temperature ki value return kare.
# 2. `set_temperature(self, value)` -> Jo temperature badle, lekin sirf tab 
#    jab value 18 aur 30 degrees ke darmiyan (`and` operator) ho.
class Thermostat():
    def __init__(self , temp = 22):
        self.__temp = temp
    def get_temp(self):
        return self.__temp
    def set_temp(self, new_temo):
        if new_temo >= 18 and new_temo <= 30:
            self.__temp = new_temo
        else:
            print("Temp 18 say 30 degree k darmyan ho.")
t = Thermostat()
print(t.get_temp())
t.set_temp(23)
print(t.get_temp())
t.set_temp(2)

# ---------------------------------------------------------------------
# 🔴 HARD LEVEL
# ---------------------------------------------------------------------

# QUESTION 4: Secret Agent Gatekeeper (Getter with Security Passcode)
# Ek class banayein `SpyProfile` jisme private name `self.__real_name = "Agent Khan"`.
# Hamein iska asli naam bahaar nikalna hai lekin muft mein nahi!
# Ek getter function banayein: `get_agent_name(self, passcode)`.
# Is function ke andar check karein: Agar bahar se bheja gaya passcode 
# exactly "UOG123" ke barabar hai, to hi asli naam return kare,
# warna screen par print kare: "Wrong Passcode! Access Denied ❌".
class SpyProfile():
    def __init__(self , name = "Agent Khan"):
        self.__name = name
    def get_agent_name(self,pc):
        if pc == "UOG123":
            print("Agent name = " , self.__name)
        else:
            print("Wrong Passcode! Access Denied")
sp = SpyProfile()
sp.get_agent_name("UOG123")
sp.get_agent_name("UOG1")

# QUESTION 5: Company Vault Guard (Protected vs Private)
# Python mein single underscore `_` protected ke liye aur double `__` private ke liye hota hai.
# Ek class banayein `CompanyVault`. Constructor mein do variables rakhein:
# 1. `self._tax_rate = 10` (Protected variable)
# 2. `self.__balance = 50000` (Private variable)
# Baahir class ke ek object banayein. Direct dono variables ko bahaar print 
# karne ki koshish karein aur comment mein batayein ke kis variable par error aaya!
class CompanyVault():
    def __init__(self , tax_rate = 10 , balance = 50000):
        self._tax_rate = tax_rate
        self.__balance = balance
cw = CompanyVault()
print("Protected = " , cw.tax_rate)
print("Private = " , cw.balance)

# QUESTION 6: Supermarket Profit Guard (Interacting with Private Data)
# Ek class banayein `OnlineItem` jisme item ka name, public selling_price ho.
# Aur ek private cost_price (`self.__cost_price`) constructor mein aaye.
# 1. Ek method banayein `get_profit(self)` jo public selling_price mein se 
#    private cost_price minus kar ke bacha hua profit return kare.
# 2. Ek setter banayein jo cost_price ko badle par zero ya minus mein na badalne de.
# Testing: Burger keemat kharid 100 aur keemat frokht 150 par chalaein.
class OnlineItem():
    def __init__(self, name , sellp , costp):
        self.name = name
        self.sellp = sellp
        self.__costp = costp
    def get_profit(self):
        return self.sellp - self.__costp
    def set_costp(self,p):
        if p > 0:
            self.__costp = p
            print("New price = " , self.__costp)
        else:
            print("Invalid cost.")
bu = OnlineItem("Burger" , 200, 170)
print(bu.get_profit())
bu.set_costp(180)
bu.set_costp(-90)