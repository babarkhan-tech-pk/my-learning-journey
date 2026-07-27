# =====================================================================
# TOPIC: PROCEDURAL PROGRAMMING & ALGORITHMS (Logic, Search & Sorting)
# TOTAL QUESTIONS: 6 (1 Easy, 2 Medium, 3 Hard)
# INSTRUCTIONS: Write your Python code below each comment block.
# =====================================================================

# ---------------------------------------------------------------------
# 🟢 EASY LEVEL
# ---------------------------------------------------------------------

# QUESTION 1: The Linear Morning Routine (Procedural Flow)
# Procedural programming mein code top-to-bottom chalta hai.
# Teeno alag alag functions banayein:
# 1. wake_up(), jo "Uth jao bacho!" print kare.
# 2. make_breakfast(), jo "Anday parathay ka nashta tayaar hai 🍳" print kare.
# 3. go_to_university(), jo "UOG ke liye rawana!" print kare.
# In teeno ko aakhri mein sahi tarkeeb se call kar ke flow dikhaein.
def wake_up():
    print("Uth jao bacho!")
def make_breakfast():
    print("Anday parathay ka nashta tayaar hai")
def go_to_university():
    print("UOG ke liye rawana!")
wake_up()
make_breakfast()
go_to_university()

# ---------------------------------------------------------------------
# 🟡 MEDIUM LEVEL
# ---------------------------------------------------------------------

# QUESTION 2: The Missing Roll Number (Linear Search Algorithm)
# Aapke paas ek list hai: roll_numbers = [12, 45, 7, 23, 90, 15]
# User se ek number input lein jo wo dhoondna chahta hai.
# Bina kisi built-in method (.index()) ke, ek FOR loop chalayein.
# Aik aik kar ke check karein, agar number mil jaye to uski seat 
# (index) batayein aur loop ko break kar dein.
# Agar poori list mein number na mile, to kahein "Bacha absent hai!".
roll_numbers = [12, 45, 7, 23, 90, 15]
found = False
user = int(input("Enter a number to search: "))
for idx , rl in enumerate(roll_numbers):
    if rl == user:
        print("Mil gya. At Index : " , idx)
        found = True
        break
if found == False:
    print("Bacha absent hy.")


# QUESTION 3: The Topper Finder (Find Maximum Algorithm)
# Ek teacher ke paas 5 bacho ke marks hain: marks = [65, 88, 42, 95, 70]
# Hamein class ka sab se bada (Maximum) score pata karna hai.
# Bina max() function ke, pehle ek variable banayein: highest = marks[0]
# Loop chalakar har mark ko "highest" se compare karein.
# Agar koi mark bada mile, to "highest" ko badal dein.
# Aakhir mein sab se bada score print karein.
marks = [65, 88, 42, 95, 70]
highest = marks[0]
for m in marks:
    if m > highest:
        highest = m
    else:
        pass
print("Highest number = " , highest)

# ---------------------------------------------------------------------
# 🔴 HARD LEVEL
# ---------------------------------------------------------------------

# QUESTION 4: Cricket Scores Sort (Bubble Sort Algorithm)
# Ek match mein Pakistani batsmen ne ye runs banaye: runs = [45, 12, 85, 0]
# Aapne in runs ko chote se bade ki taraf (Ascending Order) lagana hai.
# Bina sorted() ya .sort() ke, Bubble Sort ka algorithm likhein.
# Nested loops ka use karein. Agar pehla number agle number se 
# bada ho, to un dono ki seats aaps mein badal (swap) dein.
# Final saaf suthri sorted list screen par dikhaein.
runs = [45, 12, 85, 0]
new = []
temp = runs[0]
for i in runs:
    for j in runs:
        if i > j:
            temp = i
            i = j
            j = temp
        else:
            pass
        new.append(i)
        new.append(j)
print(new)

# QUESTION 5: Project Group Arrangement (Factorial Algorithm)
# Aapke paas project group ke 4 members hain. Aap dekhna chahte hain
# ke in bacho ko presentation ke liye kitne tarike se khara kiya 
# ja sakta hai (yani 4 ka Factorial nikalna hai: 4 x 3 x 2 x 1).
# Ek function banayein: `calculate_factorial(n)`
# Loop ya procedure ka use kar ke factorial calculate karein.
# Yaad rakhein, 0 ya 1 ka factorial hamesha 1 hota hai!
def calculate_factorial(n):
    fact = 1
    if n < 0:
        return 0
    if n == 0 or n == 1:
        return 1
    for i in range(1,n+1):
        fact = fact * i
    return fact
print(calculate_factorial(4))

# QUESTION 6: The Smart Fiber Pattern (Fibonacci Algorithm)
# Ek data analyst ko ek special pattern ke numbers chahiye.
# Pehle do numbers fix hain: 0 aur 1. Agla number hamesha 
# pichle do numbers ko plus kar ke banta hai (0, 1, 1, 2, 3, 5, 8...).
# User se input lein ke usay kitne numbers chahiye (e.g., 6).
# While ya For loop ka use kar ke utne Fibonacci numbers 
# generate karein aur unhein ek list mein daal kar print karein.
fb = [0]
count = 2
first = 0
second = 1
user = int(input("Ap ko kitny number chayie hain? "))
for count in range(user):
    sum = first + second
    fb.append(sum)
    second = first
    first = sum
print("List : " , fb)