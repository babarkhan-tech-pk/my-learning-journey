# =====================================================================
# TOPIC: TESTING IN PYTHON USING THE ASSERT KEYWORD
# TOTAL QUESTIONS: 6 (1 Easy, 2 Medium, 3 Hard)
# INSTRUCTIONS: Write your Python code below each comment block.
# =====================================================================

# ---------------------------------------------------------------------
# 🟢 EASY LEVEL
# ---------------------------------------------------------------------

# QUESTION 1: Pocket Money Balance Check
# Aapne ek variable banaya: pocket_money = 200.
# Ek aam `assert` statement ka use kar ke 
# check karein ke pocket_money 0 se bari (> 0) hai.
# Agar shart sach hai to agay "All Good" print ho.
# Yeh aapka pehla simple safety check hai!
pm = 20
assert pm > 100
print("Yes money 100 say ziada hay.")

# ---------------------------------------------------------------------
# 🟡 MEDIUM LEVEL
# ---------------------------------------------------------------------

# QUESTION 2: University Entry Age Tester
# Ek function banayein: `is_adult(age)`.
# Yeh function age return karega. Ab isko test karne 
# ke liye niche `assert` lagayein ke `is_adult(20)` 
# hamesha 18 se bada ya barabar (>= 18) hi return kare.
# Agar koi galti ho to custom message bhi trigger ho.
def is_adult(age):
    try:
        assert age >= 18
        print("Ap ka admission ho gya.")
        return age
    except AssertionError as ae:
        print("Ap ki age 18 say kam hay. ap ka admission nai ho skta.")
    except Exception as e:
        print("Error aa gya : " , e)
is_adult(27)
is_adult(17)

# QUESTION 3: Safe Discount Calculator
# Ek function banayein: `apply_discount(price, discount)`.
# Yeh price mein se discount minus kar ke final price dega.
# Niche `assert` lagakar test karein ke agar price 1000 hai 
# aur discount 200 hai, to final jawab exactly 800 hi aaye.
def apply_discount(price, discount):
    return price - discount
assert apply_discount(1000,200) == 800

# ---------------------------------------------------------------------
# 🔴 HARD LEVEL
# ---------------------------------------------------------------------

# QUESTION 4: Grade System custom Hooter (Assert with Error Message)
# Ek function banayein `get_grade(marks)`. Agar marks 90 ya
# us se zyada hon to wo string "A" return karta hai.
# Is baar `assert` ke sath comma `,` lagakar custom error
# message likhein: "Galti! Grade sahi nahi mila!".
# Test karein ke 95 marks par "A" grade hi mil raha hai.
def get_grade(marks):
    if marks > 90:
        return "A"
    return "F" 
assert get_grade(95) == "A" , "Galat grade."
assert get_grade(87) == "A" , "Galat Grade."
print("Test passed.")

def get_grade(marks):
    if marks >= 90:
        return "A"
    return "F"
# Assert ke sath apna custom error message jor diya
assert get_grade(95) == "f", "Galti! Grade sahi nahi mila! ❌"
print("Test Passed: Topper ko A grade hi mila!")

# QUESTION 5: ATM Safe Cash Withdrawal Tester
# ATM machine ka function hai: `withdraw(balance, amount)`.
# Yeh function balance mein se amount minus karta hai.
# Hamein test karna hai ke amount kabhi balance se bari na ho.
# Function ke andar hi `assert amount <= balance` lagayein
# aur sath message likhein: "Incalculable: Paise kam hain!".
# Baahir 5000 balance aur 6000 withdrawal de kar test karein.
def withdraw(balance, amount):
    return balance - amount

def withdraw(balance, amount):
    # Function ke andar hi deewar khari kar di
    assert amount <= balance, "Incalculable: Account mein paise kam hain! 🛑"
    return balance - amount
# Test 1: Sahi transaction
print("Baqi paise:", withdraw(5000, 2000))
# Test 2: Galat transaction (Yeh AssertionError throw karega)
try:
    print(withdraw(5000, 6000))
except AssertionError as error:
    print("Caught Error:", error)

# QUESTION 6: University Project Group Member Finder
# Aapke project group ki ek list hai: members = ["Babar", "Arshma", "Nida"]
# Ek test condition likhein jahan `assert` aur `in` keyword
# ka use kar ke check karein ke "Babar" list mein mojud hai.
# Phir aik aur assert likhein jo check kare ke "Zeeshan" list
# mein mojud hai, aur False hone par AssertionError dekhein.
members = ["Babar", "Arshma", "Nida"]
assert "Babar" in members
print("Test 1 passed.")
assert "Zeeshan" in members , "Ye member list ma mojod nai hay."