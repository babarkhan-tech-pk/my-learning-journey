# =====================================================================
# TOPIC: USER-DEFINED MODULES IN PYTHON (Creating and Importing Files)
# TOTAL QUESTIONS: 6 (1 Easy, 2 Medium, 3 Hard)
# INSTRUCTIONS: Imagine you have two separate files in the same folder.
# Write your Python code answers directly in the chat below.
# =====================================================================

# ---------------------------------------------------------------------
# 🟢 EASY LEVEL
# ---------------------------------------------------------------------

# QUESTION 1: The Fast-Food Bill Calculator
# Farz karein aapne ek file banai hai jis ka naam hai `billing.py`.
# Us file ke andar aapne ek function likha hai: `calculate_bill(price, qty)`.
# Ab aap apni asli file `main.py` ke andar khare hain.
# `import billing` ka use kar ke us file ko import karein, aur
# Burger keemat 250 aur quantity 3 ka bill nikal kar print karein.
import billing as b
print(b.calculate_bill(250,3))

# ---------------------------------------------------------------------
# 🟡 MEDIUM LEVEL
# ---------------------------------------------------------------------

# QUESTION 2: The Currency Exchanger with Nickname (Alias)
# Farz karein aapne ek file banai hai jis ka naam hai `converter.py`.
# Uske andar ek function mojud hai: `pkr_to_usd(rupees)`.
# Apni main file mein is module ko ek chota nick-name (Alias) 
# dein, bilkul is tarah: `import converter as conv`.
# Phir `conv.pkr_to_usd(2800)` chalakar dollars ka jawab print karein.
import billing as b
print(b.pkr_to_usd(2800))

# QUESTION 3: Specific University Greeting (From Keyword)
# Farz karein aapke paas ek bari file hai: `uog_wishes.py`.
# Usme do functions hain: `welcome_admin()` aur `welcome_student()`.
# Hamein poori file nahi chahiye, sirf bacho wala function chahiye.
# `from uog_wishes import welcome_student` ka use kar ke sirf ek 
# function import karein aur usay "Babar" naam de kar call karein.
from billing import welcome_student as ws
ws("Babr")
ws("Zeeshan")

# ---------------------------------------------------------------------
# 🔴 HARD LEVEL
# ---------------------------------------------------------------------

# QUESTION 4: Smart Attendance Scanner (Passing Lists to Custom Modules)
# Farz karein aapke paas ek file hai jis ka naam hai `attendance_helper.py`.
# Uske andar ek function mojud hai: `count_presents(attendance_list)`.
# Yeh function list mein se 'Present' ko count kar ke return karta hai.
# Apni main file mein bacho ki list banayein, is module ko import karein,
# aur list pass kar ke total haazir bacho ka score baahir print karein.
from billing import count_presents as cp
al = ["Present" , "Present" , "Absent","Present" , "Present" , "Absent"]
print("Total presents = ",cp(al))

# QUESTION 5: Secure Password Protector (Module inside a Loop)
# Farz karein aapke paas ek file hai jis ka naam hai `security.py`.
# Usme ek function hai: `check_password(user_input)` jo password verify 
# kar ke True ya False (Boolean value) return karta hai.
# Apni main file mein ek `while` loop chalayein jo user se input maangta 
# rahe aur is custom module ki madad se password sahi hone tak chalta rahe.
from billing import check_password as cp
c = False
while c == False:
    user = input("Enter password: ")
    c = cp(user)
    if c == False:
        print("Wrong pass. Try again.")
print("Account Blocked.")

# QUESTION 6: The Secret Execution Guard (if __name__ == "__main__")
# Ek professional developer banna hai to ye concept seekhna lazmi hai!
# Ek module file banayein `database.py`. Hum chahte hain ke jab is file ko 
# direct run kiya jaye to print ho: "Running Database Directly!".
# Lekin jab isay `main.py` mein import kiya jaye, to kuch bhi auto-run na ho.
# `if __name__ == "__main__":` ka sahi istemal kar ke ye guard lagayein.
from billing import connect_db as cd
cd()