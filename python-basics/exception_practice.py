# =====================================================================
# TOPIC: EXCEPTION HANDLING IN PYTHON (try, except, else, finally, raise)
# TOTAL QUESTIONS: 6 (1 Easy, 2 Medium, 3 Hard)
# INSTRUCTIONS: Write your Python code below each comment block.
# =====================================================================

# ---------------------------------------------------------------------
# 🟢 EASY LEVEL
# ---------------------------------------------------------------------

# QUESTION 1: Chocolate Divider (ZeroDivisionError)
# Aapke paas 10 chocolates hain. User se poochein
# ke kitne bacho mein baantni hain. Agar user 0
# likhe, to program crash hone ki bajaye handle kare
# aur print kare: "0 bacho mein nahi baanti ja sakti! 🍫"
# Hint: ZeroDivisionError ko except mein handle karein.
user = float ( input("KItnay bacho ma 10 chocolates bantni hain? ") )
try:
    ans = 10 / user
    print(ans , " har bachy ko mily gi.")
except ZeroDivisionError as zde:
    print("Error : " , zde)
    print("Zero cannot be devided by a number.")
except Exception as e:
    print("Error : " , e)
    print("Error Class : " , e.__class__.__name__)
    print("Something another went wrong.")

# ---------------------------------------------------------------------
# 🟡 MEDIUM LEVEL
# ---------------------------------------------------------------------

# QUESTION 2: Smart Age Input Guard (ValueError)
# Aap ek driving license form bana rahe hain.
# User se uski age input lein aur int() mein badlein.
# Agar user galti se koi text (e.g., "Twenty") likh de,
# to try-except ka use kar ke crash bachayein aur kahein:
# "Meharbani kar ke sirf numbers likhein! 🔢".
user = input("Apni age enter karen? ")
try:
    user = int(user)
    print("Ap ki age " , user , " hay.")
except Exception as e:
    print("Something went wrong.")
    print("Error : " , e)
    print("Error Class : " , e.__class__.__name__)

# QUESTION 3: Project Group Index Searcher (IndexError)
# Aapke group members ki list hai: members = ["Babar", "Arshma", "Nida"]
# User se ek seat number (index) input lein (e.g., 0, 1, 2, 5).
# Try block mein ja kar us index ka member print karein.
# Agar user 5 likhe (jo list se baahir hai), to IndexError
# ko pakrein aur kahein: "Yeh member group mein nahi hai!".
members = ["Babar", "Arshma", "Nida"]
index = int(input("Index enter karen? "))
try:
    if members[index] in members:
        print("Member name = " , members[index])
except Exception as e:
    print("Something went wrong.")
    print("Error : " , e)
    print("Error class : " , e.__class__.__name__)

# ---------------------------------------------------------------------
# 🔴 HARD LEVEL
# ---------------------------------------------------------------------

# QUESTION 4: The Ultimate Safe Calculator (Multiple Exceptions)
# User se do numbers input lein aur pehle ko doosre par divide karein.
# Is baar aapne EK SATH do khatre handle karne hain:
# 1. Agar user text likhe to ValueError pakrein.
# 2. Agar user 0 se divide kare to ZeroDivisionError pakrein.
# End mein `finally` block lagayein jo hamesha print kare:
# "Calculator Task Completed. 🧮".
n1 = int(input("Enter number 1 : "))
n2 = int(input("Enter number 2 : "))
try:
    print(n1 , " / " , n2 , " = " , n1/n2)
except ValueError as ve:
    print("Error : " , ve)
except ZeroDivisionError as zde:
    print("Error : " , zde)
except Exception as e:
    print("Something went wrong.")
    print("Error : " , e)
    print("Error class : " , e.__class__.__name__)
    

# QUESTION 5: Secret Database Key Lookup (KeyError with else)
# Ek student ka data dictionary mein hai: data = {"name": "Babar", "id": 101}
# User se poochein ke wo kya dhoondna chahta hai (e.g., "name" ya "GPA").
# Try block mein `data[user_input]` ko print karne ki koshish karein.
# Agar key na mile to KeyError pakar kar batayein ke data mojud nahi.
# Agar koi error NA AAYE, to `else` block se kahein: "Search Successful! ✅".
data = {"name": "Babar", "id": 101}
user = input("Ap kia search krna chahty hain? ")
try:
    print(data[user])
except KeyError as ke:
    print("Error : " , ke)
except Exception as e:
    print("Something went wrong.")
    print("Error : " , e)
    print("Error class : " , e.__class__.__name__)

# QUESTION 6: University Admission Merit Guard (The raise Keyword)
# Aap university admission ke liye aik automatic checkpost bana rahe hain.
# User se uska GPA input lein (float mein).
# If condition chalayein: Agar GPA 2.0 se kam (< 2.0) hai,
# to `raise` keyword ka use kar ke khud se ek ValueError paida karein
# jisme message likha ho: "Admission Denied: GPA boht kam hai! ❌".
# Is poore khel ko try-except mein wrap kar ke error message print karein.
try: 
    gpa = float(input("Enter GPA : "))
    if gpa < 2.0:
        raise ValueError("Admission denied. GPA boht kam hay.")
    else:
        print("Mubabrk ho ap ka admission ho gya hay.")
except Exception as e:
    print("Something went wrong.")
    print("Error : ",e)
    print("Error class : " , e.__class__.__name__)