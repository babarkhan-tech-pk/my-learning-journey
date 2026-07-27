# =====================================================================
# TOPIC: PYTHON FILE HANDLING (Open, Read, Write, Append & Context Managers)
# TOTAL QUESTIONS: 6 (1 Easy, 2 Medium, 3 Hard)
# INSTRUCTIONS: Write your Python code below each comment block.
# =====================================================================

# ---------------------------------------------------------------------
# 🟢 EASY LEVEL
# ---------------------------------------------------------------------

# QUESTION 1: The Secret Diary Reader
# Farz karein aapki computer mein ek file pehle se bani hai:
# "diary.txt" aur usme likha hai: "Python is awesome!".
# Python ke open() function ka use kar ke is file ko 
# "r" (Read) mode mein kholein, iska sara data parh kar 
# screen par print karein, aur file ko close() karna na bhoolein.
with open('diary.txt','r') as file:
    print(file.read())

# ---------------------------------------------------------------------
# 🟡 MEDIUM LEVEL
# ---------------------------------------------------------------------

# QUESTION 2: Ammi's Digital Grocery List Finder
# Aapne Ammi ke liye ek naya saaf suthra register banana hai.
# "grocery.txt" ke naam se ek nayi file banayein "w" (Write) mode mein.
# Is file ke andar ye teeno items alag alag line par likhein:
# "Aloo\n", "Piyaz\n", "Tamatar\n".
# Yaad rakhein, "w" mode purani file ka data saaf kar deta hai!
with open('diary.txt','w') as file:
    file.write("Aloo\n")
    file.write("Piyaz\n")
    file.write("Tamatar\n")

# QUESTION 3: Attendance Sheet Extender (Append Mode)
# Ek file pehle se bani hai "attendance.txt" jisme kuch naam hain.
# Aapne list ke aakhir mein apna naam shamil karna hai.
# File ko "a" (Append) mode mein kholein aur uske andar 
# apna naam "\nBabar Khan" write karein.
# Check karein ke purana data zinda hai ya nahi.
with open('diary.txt','a') as file:
    file.write("\nBabar Khan")

# ---------------------------------------------------------------------
# 🔴 HARD LEVEL
# ---------------------------------------------------------------------

# QUESTION 4: Smart Class Roll Call (Line-by-Line Reader)
# Ek file hai "students.txt" jisme boht saare bacho ke naam hain.
# Aapne saari file aik sath nahi parhni, balkay for loop ka 
# istemal karte hue file ko line-by-line parhna hai.
# Har line ko print karte waqt .strip() ka use karein 
# taake faltu khali spaces aur newlines (\n) khatam ho jayein.
with open('diary.txt','r') as file:
    for line in file:
        print(line.strip())

# QUESTION 5: Super Safe Project Logger (With Statement)
# Professional developers kabhi bhi aam open-close use nahi karte.
# Wo hamesha Context Manager yani `with open(...)` use karte hain.
# `with` statement ka use kar ke "project_log.txt" ko "w" mode mein kholein,
# usme likhein "Database Connected Successfully", aur check karein ke 
# kya isme file khud hi automatic close hoti hai ya nahi.
with open('diary.txt','w') as file:
    file.write("Database Connected Successfully")

# QUESTION 6: Secure File Scanner (File + Exception Handling)
# Aap ek file dhoond rahe hain jo shaayd computer mein mojud hi nahi hai.
# Try-Except block ka use karte hue "secret_code.txt" ko parhne ki koshish karein.
# Agar file computer mein nahi milti, to `FileNotFoundError` ko pakrein
# aur screen par crash hone ki bajaye khoobsurat warning message dikhaein:
# "Alert! Yeh file computer mein mojud nahi hai! 🛑".
try:
    with open("dairy.txt",'r') as file:
        file.read()
except FileNotFoundError as fne:
    print("Your file does not exist.")
    print("Error : " , fne)
except Exception as e:
    print("SOmething went wrong.")
    print("Error : " , e)
    print("Error class : " , e.__class__.__name__)