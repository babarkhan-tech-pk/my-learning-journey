# Easy Level (Aasaan Sawal)
# 1. Mobile Phone Charging Screen
alarm = input("Kya aap uth gaye hain? (Yes/No) ")
alarm.lower()
while (alarm != "yes"):
    alarm = input("Kya aap uth gaye hain? (Yes/No) ")
    alarm.lower()
print("Good Morning")

# 4. ATM PIN Verification
pin = int(input("Enter your pin? "))
while( pin != 1234):
    print("Galat PIN! Dobara koshish karein.")
    pin = int(input("Enter your pin? "))
print("Access Granted.")

# 7. Smart Password Locker (Max 3 Attempts)
count = 0
pin = int(input("Enter your pin? "))
while( pin != 1234):
    count += 1
    if count == 3:
        print("Account blocked.")
        break
    else:
        print("Galat PIN! Dobara koshish karein.")
        pin = int(input("Enter your pin? "))

# 10. Unlimited Tea Stall (While True & Break)
chai = input("Kya aapko aur chai chahiye? (Yes/No) ")
chai = chai.lower()
while ( chai != "no"):
    chai = input("Kya aapko aur chai chahiye? (Yes/No) ")
    chai = chai.lower()
print("Good bye")