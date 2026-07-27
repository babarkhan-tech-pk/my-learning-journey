# 1. Fast-Food Bill & Free Delivery Check
price = float (input("Enter price ? "))
quantity = int (input("Enter quantity? "))
bill = price * quantity
if bill > 1500:
    print(f"Mubarak ho! Aapko free delivery milegi. Kul bill: {bill}")
else:
    bill += 150
    print(f"Total bill = {bill}")

# 6. Custom Star Carpet Designer
row  = int(input("Ap ko kitni rows chayie? "))
col = int(input("Ap ko kitnay columns chahyie? "))
for i in range(row):
    for j in range(col):
        print("*" , end = " ")
    print()
    

# 8. School Exam Merit List Checker
lists = [['Babar', 85, 90], ['Zeeshan', 45, 70], ['Arshma', 95, 100]]
for s in lists:
    name = s[0]
    math = s[1]
    prog = s[2]

if math > 50 and prog > 50:
    print(f"{name} , You are pass.")

# 10. Restaurant Multi-Table Bill System
for i in range (2):
    print(f"Table {i}")
    b = int(input("Enter amount : "))
    while ( b != 0):
        b = int(input("Enter amount : "))