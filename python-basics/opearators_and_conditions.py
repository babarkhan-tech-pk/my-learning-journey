# Easy Level (Aasaan Sawal)
# 1. Amusement Park Ride Ticket
height = float (input("Bacha apni height enter karen? "))
if (height > 4.0):
    print("Aap ride par baith sakte hain!")
else:
    print("Aap abhi chote hain!")

# 2. Chocolate Distribution Day
chocolates = int(input("Ap k pas kitni chocolates hain? "))
if chocolates % 2 == 0:
    print("Barabar baanti ja sakti hain!")
else:
    print("Aik chocolate bach jaye gi!")

# 3. Supermarket Discount Check
bill = int(input("Ap ka bill kitna hay? "))
if bill > 1000:
    print("Mubarak ho! Aapko discount milega.")
else:
    print("Discount ke liye thodi aur shopping karein.")

# Medium Level (Darmiyane Sawal)
# 4. Traffic Light Signal Simulator
signal = input("Signal enter karen? ")
signal = signal.lower()
if signal == "red":
    print("Ruk jayein!")
elif signal == "yellow":
    print("Tayyar ho jayein!")
elif signal == "green":
    print("Chalein jayein!")
else:
    print("Galt signal!")

# 5. School Grading System
marks = int(input("Marks kitny hain? "))
if marks >= 90:
    print("Grade A")
elif marks >= 75 and marks <= 89:
    print("Grade B")
elif marks >=50 and marks <= 74:
    print("Grade C")
else:
    print("Grade F")

# 6. Cinema Ticket Pricing
age = int(input("Ap ki age kia hay? "))
if age < 12:
    print("300 Rupees")
elif age >= 12 and age <= 60:
    print("600 Rupees")
else:
    print("400 Rupees")

# Hard Level (Mushkil Sawal)
# 7. Smart ATM Cash Withdrawal
balance = float(input("Ap ka balance kitan hay? "))
amount = float (input("Ap nay kitni amount niklwani hay? "))
if amount <= balance:
    if amount % 500 == 0:
        print("Paisay nikal rahy hain.")
    else:
        print("Transction fail. Enter the multiple of 500.")
else:
    print("Ap k pass itni amount nahi hay.")

# 8. Food Delivery Free Shipping App
bill = int(input("AP ka bill kitna hay? "))
membership = input("KIa ap hmary premium member hain? (True / False) ")
membership = membership.lower()
if bill > 2000 or membership == "true":
    print("Delivery Free!")
else:
    print("Delivery charges: 200 Rupees")

# 9. Uber Peak Hours Price Calculator
peakHours = input("KIa abhi peak hours hain? (True / False) ")
peakHours = peakHours.lower()
mosam = input("KIa abhi mosam khrab hay hain? (True / False) ")
mosam = mosam.lower()
if peakHours == "true"  and mosam == "true" :
    print("Double (2x)")
elif peakHours == "true"  or mosam == "true" :
    print("Normal se thoda zyada (1.5x)")
else:
    print("Normal")

# 10. University Scholarship Advisor
gpa = float(input("Enter your gpa: "))
attendance = int(input("Enter your attendance percantage : "))
if gpa > 3.8:
    print("Mubarak ho! Super Scholarship mili.")
elif gpa >= 3.5 and gpa <= 3.79 and attendance > 85:
    print("Aapko Standard Scholarship mili.")
else:
    print("Sorry, aap eligible nahi hain.")