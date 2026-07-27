# =====================================================================
# TOPIC: VARIABLE SCOPE IN PYTHON (LEGB Rule: Local, Enclosed, Global, Built-in)
# TOTAL QUESTIONS: 6 (1 Easy, 2 Medium, 3 Hard)
# INSTRUCTIONS: Write your Python code below each comment block.
# =====================================================================

# ---------------------------------------------------------------------
# 🟢 EASY LEVEL
# ---------------------------------------------------------------------

# QUESTION 1: The University Bag Check (Local vs Global)
# Ek global variable banayein: campus_name = "UOG Kharian".
# Ab ek function banayein: student_bag(). Inside function,
# ek local variable rakhein: secret_diary = "Data Science Notes".
# Function ke andar dono variables ko print karne ki koshish karein.
# Phir function ke baahir nikal kar campus_name print karein aur check
# karein ke kya secret_diary baahir print karne par computer error deta hai?
campus_name = "UOG Kharian"
def local():
    secret_diary = "Data Science Notes"
    print("Global = " , campus_name)
    print("Local = " , secret_diary)
local()
print("Global = " , campus_name)
#print("Local = " , secret_diary)

# ---------------------------------------------------------------------
# 🟡 MEDIUM LEVEL
# ---------------------------------------------------------------------

# QUESTION 2: The Project Group Secret (Enclosed Scope)
# Ek bada outer function banayein: project_room(). Inside it,
# ek variable banayein: group_topic = "AI Face Recognition".
# Is function ke andar ek chota inner function banayein: laptop_screen().
# Inner function ke andar bina koi naya variable banaye direct
# group_topic ko print karein aur check karein ke kya andar
# wala function bahar wale ki baat sunta hai (Enclosed Scope).
# End mein outer function ke andar hi inner function ko call karein.
def project_room():
    group_topic = "AI Face Recognition"
    def laptop_screen():
        print("Enclosed = " , group_topic)
    laptop_screen()
project_room()

# QUESTION 3: Canteen Cash Register Update (The global Keyword)
# Ek global variable banayein: total_canteen_cash = 1000.
# Ek function banayein: buy_samosa(price). Function ke andar
# haman global register ke paise update (cash = cash + price) karne hain.
# 'global' keyword ka sahi istemal karein taake computer error 
# na de aur baahir balance check karne par naya balance 1030 dikhaye.
total_canteen_cash = 1000
def buy_samosa(price):
    global total_canteen_cash
    total_canteen_cash += price
buy_samosa(30)
print("New cash = " , total_canteen_cash)

# ---------------------------------------------------------------------
# 🔴 HARD LEVEL
# ---------------------------------------------------------------------

# QUESTION 4: Project Marks Modifier (The nonlocal Keyword)
# Ek outer function banayein: semester_evaluation(). Inside it,
# ek variable rakhein: mid_marks = 30. Phir ek inner function
# banayein: teacher_grace_marks(). Hum chahte hain ke inner function
# ke andar se mid_marks ko badal kar 35 kar diya jaye.
# 'nonlocal' keyword ka use karein kyunki ye variable na to global
# hai aur na hi bilkul local. End mein updated marks print karein.
def semester_evaluation():
    mid_marks = 30
    def teacher_grace_marks():
        nonlocal mid_marks
        mid_marks += 5
    teacher_grace_marks()
    print("Marks = " , mid_marks)
semester_evaluation()
    

# QUESTION 5: The System Function Shadow Trap (Built-in Scope)
# Python ke paas apne pehle se banaye kuch built-in functions hote hain
# jaise len() ya sum(). Ek function banayein: trap_function().
# Is function ke andar jaan boojh kar ek variable banayein jis ka
# naam 'sum' ho aur usme koi number rakh dein (e.g., sum = 50).
# Phir usi function ke andar Python ka asli sum() chalane ki koshish
# karein aur dekhein ke Built-in scope kaise block (shadow) hota hai.
def trap_function():
    sum = 50
    sum()
trap_function()

# QUESTION 6: The Grand LEGB Ultimate Battle (The Execution Chain)
# Ek bada global variable banayein: score = 100.
# Ek outer function banayein jiske andar enclosed variable ho: score = 80.
# Uske andar ek inner function banayein jiske andar local variable ho: score = 50.
# Teeno jagah bilkul same variable name 'score' use karna hai!
# Inner function ke andar 'score' print karein aur batayein ke computer
# sab se pehle kis score ko uthayega aur LEGB chain kaise chalti hai.
score = 100
def outer():
    score = 80
    def inner():
        score = 50
        print(score)
    inner()
outer()