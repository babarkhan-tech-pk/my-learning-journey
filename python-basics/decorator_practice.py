# =====================================================================
# TOPIC: PYTHON DECORATORS (Function Wrappers, @ Syntax, Args & Kwargs)
# TOTAL QUESTIONS: 6 (1 Easy, 2 Medium, 3 Hard)
# INSTRUCTIONS: Write your Python code below each comment block.
# =====================================================================

import time

# ---------------------------------------------------------------------
# 🟢 EASY LEVEL
# ---------------------------------------------------------------------

# QUESTION 1: The University Welcome Border (Simple Decorator)
# Ek decorator function banayein `border_decorator(func)`.
# Iske andar ek `wrapper()` function banayein jo target function 
# chalne se pehle "====================" print kare aur baad mein bhi 
# border print kare. Target function `show_msg()` ke oopar `@border_decorator`
# lagakar usay saaf suthra chamkaayein.
def border_decorator(func):
    def wrapper():
        print("=============")
        func()
        print("=============")
    return wrapper
@border_decorator
def hello():
    print("Hello")
hello()

# ---------------------------------------------------------------------
# 🟡 MEDIUM LEVEL
# ---------------------------------------------------------------------

# QUESTION 2: Canteen Order Logger (Function Name Tracking)
# Ek decorator banayein `log_order(func)`.
# Inside wrapper, target function ka asli naam pata karne ke liye 
# `func.__name__` ka use karein aur print karein: "Executing: [func_name]".
# Phir target function ko chalayein. `@log_order` ka use kar ke 
# `make_chai()` aur `make_samosa()` dono functions ko track karein.
def log_order(func):
    def wrapper():
        name = func.__name__
        print("Executing " , name , "....")
        func()
        print("Closing " , name , "....")
    return wrapper
@log_order
def order():
    print("Ye rha order.")
order()

# QUESTION 3: Pocket Money Doubler (Modifying Return Values)
# Decorators sirf aage piche print nahi karte, wo jawab bhi badal sakte hain!
# Ek decorator banayein `double_money(func)`.
# Inside wrapper, pehle target function ko chalakar uska return jawab 
# ek variable mein save karein. Phir us jawab ko 2 se multiply (double) 
# kar ke baahir return karein. Target function `get_salary()` par test karein.
def double_shah(func):
    def wrapper():
        var = func()
        return var * 2
    return wrapper
@double_shah
def get_salary():
    return 10000
print(get_salary())

# ---------------------------------------------------------------------
# 🔴 HARD LEVEL
# ---------------------------------------------------------------------

# QUESTION 4: Security Gate Pass Controller (Decorators with Arguments)
# Jab target function mein parameters hon, to wrapper mein `*args, **kwargs` lazmi hai!
# Ek decorator banayein `secure_gate(func)`.
# Wrapper ke andar check karein: Agar arguments mein `user="Babar"` mojud hai,
# to hi function chalne dein, warna print karein: "Access Denied! ❌".
# Test karein: `enter_lab(user="Babar")` aur `enter_lab(user="Ali")`.
def secure_gate(func):
    def wrapper(*args,**kwargs):
        if kwargs.get("user") == "Babar":
            print("Access mil gya j.")
            return func(*args,**kwargs)
        else:
            print("Access nai mil skia ji.")
    return wrapper
@secure_gate
def enter_lab(user):
    print("Inside lab.")
print(enter_lab(user="Babar"))
print(enter_lab(user="Zeeshan"))

# QUESTION 5: Data Science Execution Timer (Performance Testing)
# Data science ke heavy loops kitna time lete hain, yeh check karna zaroori hai.
# Ek decorator banayein `performance_timer(func)`.
# Function chalne se pehle `start = time.time()` record karein, function chalayein,
# aur baad mein `end = time.time()` nikal kar dono ka difference (end - start) 
# screen par show karein. Isay ek lambe list loop function par test karein.
import time
def performance_timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Total time taken = " , end - start)
    return wrapper()
@performance_timer
def chk():
    for li in range(50):
        print(li)
print(chk())

# QUESTION 6: The Ultimate Smart Repeater (Decorators that take Arguments)
# Yeh pro-level decorator template hai jahan decorator khud bahar se argument leta hai!
# Ek advanced triple-nested decorator banayein: `repeat_action(num_times)`.
# Taake jab hum function ke oopar likhein `@repeat_action(num_times=3)`,
# to wo function automatic andar 3 dafa baari baari run ho jaye.
# Target function `print_naara()` par isay test kar ke dikhaein.
def repeat_action(num_times):
    def hi(func):
        def wrapper(*args, **kwargs):
            for i in range(num_times):
                func(*args,**kwargs)
        return wrapper
    return hi
@repeat_action(3)
def print_nara():
    print("Pakistan Zindabad.")
print(print_nara())