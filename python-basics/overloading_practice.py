# =====================================================================
# TOPIC: METHOD & OPERATOR OVERLOADING IN PYTHON (Dunder Methods & Args)
# TOTAL QUESTIONS: 6 (1 Easy, 2 Medium, 3 Hard)
# INSTRUCTIONS: Write your Python code below each comment block.
# =====================================================================

# ---------------------------------------------------------------------
# 🟢 EASY LEVEL
# ---------------------------------------------------------------------

# QUESTION 1: The Flexible Greeting System (Method Overloading Simulation)
# Ek class banayein `Greeter`. Isme ek method banayein `say_hello()`.
# Yeh method do tarah se chalna chahiye (Default arguments use karein):
# 1. Agar sirf name diya jaye (e.g., "Babar"), to "Hello Babar!" print kare.
# 2. Agar name ke sath custom message bhi diya jaye (e.g., "Good Morning"),
#    to "Good Morning, Babar!" print kare.
# Baahir ek hi object bana kar dono tareeqon se call karein.
class Greeter():
    def say_hello(self, name,msg = None):
        if msg is None:
            print("Hello " , name)
        else:
            print(msg, ", Hello " , name)
g = Greeter()
g.say_hello("Babar")
g.say_hello("Babar", "Good Morning Sir")

# ---------------------------------------------------------------------
# 🟡 MEDIUM LEVEL
# ---------------------------------------------------------------------

# QUESTION 2: Joint Pizza Party Bill (Operator Overloading `+`)
# Ek class banayein `PizzaBill` jisme constructor mein price aaye.
# Jab hum do pizza bills ke objects ko `+` operator se jama karein,
# to computer error dene ki bajaye dono ki prices ko plus kar de!
# Hint: Class ke andar jadui method `__add__(self, other)` likhein
# jo dono objects ki prices ko plus kar ke total return kare.
class PizzaBill():
    def __init__(self , price):
        self.price = price
    def __add__(self,other):
        return self.price + other.price
p1 = PizzaBill(1000)
p2 = PizzaBill(2000)
print("Total bill = ", p1.__add__(p2))

# QUESTION 3: Smart Area Calculator (Method Overloading with *args)
# Ek class banayein `ShapeCalculator`. Isme method banayein `calculate_area(*args)`.
# Yeh method parameters ki ginti dekh kar faisla karega:
# 1. Agar *args mein sirf 1 number aaye, to usay Square samjhe (side * side).
# 2. Agar *args mein 2 numbers aayein, to Rectangle samjhe (length * width).
# Function ke andar len(args) check kar ke dono ki math chalaein aur return karein.
class ShapeCalculator():
    def calculate_area(self, *args):
        if len(args) == 1:
            side = args[0]
            return side * side
        else:
            length = int(args[0])
            width = int(args[1])
            return length * width
s1 = ShapeCalculator()
print("Square = " , s1.calculate_area(10))
print("Rectangle = " , s1.calculate_area(10,30))

# ---------------------------------------------------------------------
# 🔴 HARD LEVEL
# ---------------------------------------------------------------------

# QUESTION 4: Student Merit List Finalizer (Operator Overloading `>`)
# University group ke do bacho ka GPA compare karna hai.
# Class banayein `Student` jisme name aur gpa constructor mein aayein.
# Jadui method `__gt__(self, other)` (Greater Than) ka use karein.
# Taake jab hum baahir likhein `if student1 > student2:`, to computer
# automatic unke GPA ko aapas mein compare kare aur bataye kaun topper hai.
class Student():
    def __init__(self , name , cgpa):
        self.name = name
        self.cgpa = cgpa
    def __gt__(self, other):
        print(self.cgpa > other.cgpa)
s1 = Student("Babar" , 3.96)
s2 = Student("Waqas",3.64)
s1.__gt__(s2)

# QUESTION 5: The Smart Money Vault (Combining `__add__` and `__str__`)
# Ek class banayein `MoneyVault` jisme constructor mein total cash save ho.
# 1. Jab hum object ko direct print karein (e.g., print(my_vault)), to
#    `__str__(self)` ka use kar ke dikhaein: "Vault has [cash] Rupees."
# 2. Jab hum do vaults ko `+` karein, to ek naya `MoneyVault` object return 
#    ho jisme dono ka total cash jama ho chuka ho. Test kar ke dikhaein.
class MoneyVault():
    def __init__(self, cash):
        self.cash = cash
    def __str__(self):
        print(f"Vault has {self.cash} Rupees.")
    def __add__(self,other):
        return self.cash + other.cash
m1 = MoneyVault(1000)
m2 = MoneyVault(2000)
m1.__str__()
print("Total cash = ",m1.__add__(m2))

# QUESTION 6: Smart Delivery Package (Overloading with Type Checking)
# Ek advanced function banayein `process_package(data)`.
# Python mein overloading check karne ke liye type() ya isinstance() use hota hai.
# 1. Agar data ki type String (`str`) hai, to "Text Message sent: [data]" print kare.
# 2. Agar data ki type Integer (`int`) hai, to "Weight recorded: [data] kg" print kare.
# 3. Agar data ki type List (`list`) hai, to loop chalakar saare items print kare.
def process_package(data):
    if type(data) == str:
        print("Text Message sent: " , data)
    elif type(data) == int:
        print("Weight recorded: " , data , " Kg.")
    elif type(data) == list:
        for i in data:
            print(i)
    else:
        print("Invalid type.")
process_package("ALlah")
process_package(90)
process_package([1,2,3,4])
process_package({1,2,3})