# =====================================================================
# TOPIC: PYTHON SETS (Uniqueness, Operations: Union, Intersection, etc.)
# TOTAL QUESTIONS: 6 (1 Easy, 2 Medium, 3 Hard)
# INSTRUCTIONS: Write your Python code below each comment block.
# =====================================================================

# ---------------------------------------------------------------------
# 🟢 EASY LEVEL
# ---------------------------------------------------------------------

# QUESTION 1: Attendance Duplicate Cleaner
# Ek university class mein bache bar bar andar baahir aa rahe hain.
# Guard ne register mein roll numbers likhe:
# roll_numbers = [101, 102, 101, 103, 102, 104, 101]
# Ghaur se dekhein, is list mein boht se roll numbers repeat ho rahe hain.
# Python ke set() function ka istemal kar ke duplicates khatam karein,
# aur screen par saaf suthre total unique bacho ki ginti print karein.
roll_numbers = [101, 102, 101, 103, 102, 104, 101]
roll_numbers = set(roll_numbers)
print(roll_numbers)

# ---------------------------------------------------------------------
# 🟡 MEDIUM LEVEL
# ---------------------------------------------------------------------

# QUESTION 2: Sports Gala Registration (Union)
# University ke sports gala mein do alag alag maseet/rooms mein 
# registrations ho rahi hain.
# Set A (Cricket): cricket_players = {"Ali", "Zain", "Babar"}
# Set B (Football): football_players = {"Zain", "Arshma", "Nida"}
# Dono sets ka Union (`|` operator ya union() method) nikalein
# taake hamein un tamam unique bacho ki list mil jaye jo kisi bhi 
# khel mein hissa le rahe hain. Final set print karein.
cricket_players = {"Ali", "Zain", "Babar"}
football_players = {"Zain", "Arshma", "Nida"}
print(cricket_players.union(football_players))
print(cricket_players | football_players)

# QUESTION 3: Common Friends Finder (Intersection)
# Aap aur aapke dost ke dosto ke do alag sets hain.
# Aapke dost: my_friends = {"Zeeshan", "Ali", "Qirat", "Umer"}
# Dost ke dost: his_friends = {"Arshma", "Ali", "Zeeshan", "Nida"}
# Dono ke darmiyan common (jo aapke bhi dost hain aur uske bhi)
# dosto ko dhoondne ke liye Intersection (`&` ya intersection())
# ka istemal karein aur unke naam screen par dikhaein.
my_friends = {"Zeeshan", "Ali", "Qirat", "Umer"}
his_friends = {"Arshma", "Ali", "Zeeshan", "Nida"}
print(my_friends.intersection(his_friends))
print(my_friends & his_friends)

# ---------------------------------------------------------------------
# 🔴 HARD LEVEL
# ---------------------------------------------------------------------

# QUESTION 4: Library Book Availability (Difference)
# Ek department ki library mein total 5 books honi chahiye thin:
# total_books = {"Python", "Data Science", "Maths", "SQL", "AI"}
# Is waqt jo books bacho ne borrow (udhaar) li hui hain wo hain:
# borrowed_books = {"Maths", "SQL"}
# Set Difference (`-` operator ya difference() method) ka use karein
# aur pata lagayein ke kaunsi books abhi bhi library mein mojud hain
# jo borrow nahi huin. Un available books ko print karein.
total_books = {"Python", "Data Science", "Maths", "SQL", "AI"}
borrowed_books = {"Maths", "SQL"}
print(total_books.difference(borrowed_books))
print(total_books - borrowed_books)

# QUESTION 5: Dynamic Whitelist Entry (Add & Discard)
# Ek system ki security ke liye aapne ek set banaya hai:
# allowed_users = {"admin", "teacher"}
# 1. user se ek naya username input lein aur set mein add() karein.
# 2. check karein, agar "guest" naam ka banda set mein mojud hai,
# to usay discard() ki madad se set se nikal bahar phekein.
# Final updated set ko screen par show karein.
allowed_users = {"admin", "teacher"}
user = input("Enter a new name? ")
allowed_users.add(user)
print(allowed_users)
allowed_users.discard("guest")
print(allowed_users)

# QUESTION 6: Exclusive Project Tools (Symmetric Difference)
# Do software development teams alag alag tools use kar rahi hain:
# team_a = {"VS Code", "Python", "SQL Server", "GitHub"}
# team_b = {"PyCharm", "Python", "MySQL", "GitHub"}
# Hamein wo tools chahiye jo dono teams mein COMMON NAHI HAIN,
# yaani jo sirf team A ya sirf team B ke paas exclusive hain.
# Symmetric Difference (`^` ya symmetric_difference()) ka use kar ke
# un exclusive tools ka set nikalein aur print karein.
team_a = {"VS Code", "Python", "SQL Server", "GitHub"}
team_b = {"PyCharm", "Python", "MySQL", "GitHub"}
print(team_a.symmetric_difference(team_b))
print(team_a ^ team_b)