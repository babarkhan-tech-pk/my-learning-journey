# Easy Level (Aasaan Sawal)
# 1. Fitness Tracker Steps Counter
for step in range(5):
    print(f"Step {step}")

# 3. Ammi ki Shopping List
shopping = ['Aloo', 'Piyaz', 'Tamatar', 'Chini']
for item in shopping:
    print(f"Bazar se le kar aana hai: {item}")

# Medium Level (Darmiyane Sawal)
# 4. Table of 5 Creator
for i in range(10):
    print (f"{i + 1} X 5 = {(i+1)* 5}")

# 6. Even Bus Numbers Filter
buses = [12, 15, 22, 37, 40, 45]
for bus in buses:
    if (bus % 2 == 0):
        print(bus)

# Hard Level (Mushkil Sawal)
# 7. Attendance Sheet Scanner
attendance = ['Present', 'Present', 'Absent', 'Present', 'Absent']
count = 0
for a in attendance:
    if a == "Present":
        count += 1
    else:
        continue
print(count)

# 8. Airport Security Bag Scanner (Break Loop)
items = ['Kapde', 'Kitab', 'Chaku', 'Perfume']
for item in items:
    if item == "Chaku":
        print("ALERT! Scanner Rok Diya Gaya Hai!")

# 10. Weekly Meal Routine (Nested Loop)
days = ['Monday', 'Tuesday']
meals = ['Breakfast', 'Dinner']
for day in days:
    for meal in meals:
        print(f"Day = {day} , Meal = {meal}")