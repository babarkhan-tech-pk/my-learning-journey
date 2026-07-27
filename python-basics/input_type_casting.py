# Easy Level (Aasaan Sawal)

# 1. The Security Guard Register
#Ek security guard society ke gate par khara hai. 
# Wo har aane wale mehman ka naam register mein likhna chahta hai. 
# Python mein ek aisa program banayein.
# jo user se uska naam pooche aur screen par print kare: "Welcome to the society, [Naam]!".
mehman = input("Sir, Aap Ka Name kia hay? ")
print(f"Welcome to the society , {mehman}.")

# 2. Birthday Cake Candle Calculator
# Ek cake shop wala bache se uska birth year (paidaish ka saal) poochta hai,
# taake cake par lagane ke liye candles count kar sake. User se uska birth year input lein, 
# usay number mein badlein, aur 2026 se minus kar ke uski age screen par dikhein.
birthYear = input("Bachy , Ap ki paidaish ka sal kon sa hay? ")
birthYear = int(birthYear)
print(f"Beta aap ki umar {2026 - birthYear} sal hay.")

# 3. Simple Shopkeeper Calculator
# Ek chota dukan daar do alag alag cheezon ki keemat (prices) computer mein daalna chahta hai, 
# taake unka total kar sake. User se do numbers input lein, 
# unhein integers (poore numbers) mein badlein, aur unka sum (total) print karein.
item1 = int(input("Item 1 ki price likhen? "))
item2 = int(input('Item 2 ki price likhen? '))
total = item1 + item2
print(f"Aap ka total bill {total} ruppees hay.")

# Medium Level (Darmiyane Sawal)

# 4. Weather Report Assistant
# Aap ek weather reporter hain. 
# Aapko temperature Celsius mein milta hai par aapne usay Fahrenheit mein badalna hai. 
# User se temperature decimal (float) mein input lein. 
# Phir ye formula lagayein: $F = (C \times 9/5) + 32$. 
# Final Fahrenheit temperature screen par show karein.
celcius = int( input("Celcius ma temprature enter karen? ") )
farenheit = ( celcius * ( 9/5 ) ) + 32
print(f"Temprature in farenheit is {farenheit}.")

# 5. Supermarket Billing Counter
# Supermarket ka cashier ek product ki price aur uski quantity (kitni cheezein khareedin) ,
# input karta hai. Yaad rakhein price decimal (float) ho sakti hai 
# aur quantity hamesha integer hoti hai. 
# Total bill calculate kar ke screen par dikhein.
price = float ( input("Product ki price kia hay? ") )
quantity = int ( input("Product ki quantity kitni hay? ") )
total_bill = price * quantity
print(f"Ap ka total bill {total_bill} hay.")

# 6. Restaurant Bill Splitter
# Aap aur aapke dost ek restaurant mein khana khate hain. 
# Total bill aata hai jo decimal mein ho sakta hai, aur aap total 4 dost hain.
# User se total bill input lein aur usay 4 par divide kar ke ,
# har dost ka hissa (share) screen par print karein.
total_bill = float( input("Total bill kitna hay? ") )
print(f"Per person {total_bill / 4} pay kary ga.")

# Hard Questions

# 7. School Report Card Generator
# Ek school teacher 3 subjects (Maths, Science, English) ke marks input karti hai 
# (jo points mein bhi ho sakte hain). Aapne un teeno marks ka average nikalna hai.
#  Phir us average score ko wapas ek string (text) mein badal kar is tarah print karna hai: 
# "Aapka final average score hai: [Average]".
maths = int( input("Math ma marks kitnay hain? "))
science = int(input("Science ma marks kitnay hain? "))
english = int(input("English ma marks kitnay hain? "))
sum = maths + science + english
avg = sum / 3
print("Aap ka final average score hai : " + str(avg))

# 8. Google Maps Distance Estimator
# Ek runner road par daor raha hai. Wo apna distance Kilometers mein input karta hai 
# (e.g., 5.5 km). Aapka program us distance ko meters (integer) mein aur miles (float) mein convert karega. 
# Phir string concatenation ya f-string use kar ke aik hi line mein pura message dikhana hai.
# (Hint: 1 km = 1000 meters, 1 km = 0.621 miles)
kilometers = float ( input("Bhai ap kitny kilometers door chuky hain? ") )
print(f"Matlab ap {kilometers * 1000} meters door chuky hain.")
miles = kilometers * 0.621
print("Or ap " + str(miles) + " miles door chukay hain.")

# 9. Exact Money Changer App
# Aap ek currency exchange app bana rahe hain. 
# User Pakistani Rupees (PKR) input karta hai. 
# Aap usay US Dollars (USD) mein convert karte hain (Farz karein 1 USD = 280 PKR). 
# Aapne screen par exact dollars (float value) bhi dikhane hain aur 
# rounded dollars (integer value) bhi show karne hain type casting ke zariye.
pkr = int(input("Ap k pass kitnay pakistani rupees hain? "))
dollar = pkr / 280
print(f"Ap k pas {dollar} dollars hain.")
dollar = int(dollar)
print("Ap k pas " + str(dollar) + " dollars hain.")

# 10. Smart Fitness Tracker
# Ek smart watch user ke do din ke steps count karti hai. 
# Kabhi kabhi user galti se decimal number daal deta hai (jaise 5000.5 steps). 
# Aapne dono din ke steps input lene hain, unhein foran integer mein convert kar ke fraction khatam karna hai,
#  dono ko plus karna hai, aur total steps ka result screen par show karna hai.
day1 = int(input("Ap day 1 ma kitny steps chaly ? "))
day2 = int(input("Ap day 2 ma kitny steps chaly ? "))
print(f"Ap 2 din ma total { day1 + day2 } steps chaly hain.")