# 1. Building Blocks Grid
for i in range(3):
    for j in range(1):
        print("* * *")

# 3. Ludo Dice Roll Combinations
for i in range(3):
    for j in range(3):
        print(f"{i} - {j}")

# 6. Math Tables Matrix (2 to 4)
for i in range (2,5):
    for j in range(1,6):
        print(f" {i} X {j} = {i * j}")

# 7. Security Guard VIP Room Scanner (With Skip)
for i in range(3):
    for j in range(3):
        if i == 2 and j == 2:
            continue
        else:
            print(f"Floor {i} , Room {j}")

# 10. Secret Password Cracker (Double Break)
pass1 = "AB"
pass2 = "AB"
for p1 in pass1:
    for p2 in pass2:
        if p1 == "B" and p2 == "A":
            print("Password Found!")
            break
        print("Fonding..")


names = ["Anna", "Natasha", "Mike"]
names.insert(2, "Xi")
print(names)

for x in range(1, 4):
    print(int((str((float(x))))))

class A:
   def a(self):
       return "Function inside A"

class B:
   def a(self):
       return "Function inside B"

class C:
   pass

class D(C, A, B):
   pass

d = D()
print(d.a())