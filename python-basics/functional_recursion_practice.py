# =====================================================================
# TOPIC: FUNCTIONAL PROGRAMMING & RECURSION (Lambda, Pure Functions, Recursion)
# TOTAL QUESTIONS: 6 (1 Easy, 2 Medium, 3 Hard)
# INSTRUCTIONS: Write your Python code below each comment block.
# =====================================================================

# ---------------------------------------------------------------------
# 🟢 EASY LEVEL
# ---------------------------------------------------------------------

# QUESTION 1: The Microwave Beep Countdown (Simple Recursion)
# Aap ek smart microwave ka timer software bana rahe hain.
# `def microwave_countdown(seconds)` naam ka ek recursive function banayein.
# Agar seconds 0 par pahuchein, to print kare: "Beep! Khana garam ho gaya! 🍲"
# Warna, current second print kare aur khud ko (seconds - 1) de kar 
# dobara call kare. Isay 3 seconds de kar test karein.
def microwave_countdown(seconds):
    if seconds == 0:
        print("Beep! Khana garam ho gaya!")
    else:
        print(seconds)
        return microwave_countdown(seconds - 1)
microwave_countdown(10)

# ---------------------------------------------------------------------
# 🟡 MEDIUM LEVEL
# ---------------------------------------------------------------------

# QUESTION 2: Petrol Price Tax Calculator (Lambda & Map)
# Petrol ki purani prices ki ek list hai: old_prices = [250, 270, 280]
# Govt ne har litre par 10 rupees tax barha diya hai.
# Python ke `lambda` aur `map()` function ka aik sath istemal karein.
# Ek hi line mein saari prices mein 10 plus kar ke nayi list banayein.
# Final updated prices ki list ko screen par print karein.
old_prices = [250, 270, 280]
def add_price(pr):
    return pr + 10
map_list = map(add_price(old_prices),old_prices)
print("OLD PRICES : " , old_prices)
print("New prices : " , map_list)

# QUESTION 3: Pocket Money Staircase (Recursive Summation)
# Ek bacha rozana apni pocket money barhata hai. Pehle din 1 rupee,
# doosre din 2 rupees, teesre din 3 rupees... up to N days.
# `def recursive_savings(days)` naam ka ek function banayein.
# Agar days 1 ho, to 1 return kare (Base Case).
# Warna, current day ko pichle dinon ki savings mein plus kar ke
# recursive call kare. 5 dino ki total savings pata karein.
def recursive_savings(days): # 5
    savings = 0 # 0
    if days == 1: # false , 
        return 1
    return days + recursive_savings(days - 1) # 4 , 
print(recursive_savings(5))

# ---------------------------------------------------------------------
# 🔴 HARD LEVEL
# ---------------------------------------------------------------------

# QUESTION 4: Secret Spy Message Reverser (Recursive String Reversal)
# Aap ek khufia agency ke liye kaam kar rahe hain aur message ulta karna hai.
# `def reverse_message(text)` naam ka ek recursive function banayein.
# Base Case: Agar string khali "" ho ya uski lambai 1 ho, to wahi return kare.
# Recursive Case: String ka pehla akshar (character) aakhir mein jorein
# aur baqi bache text ko dobara function mein bhej dein.
# Testing ke liye "babar" bhej kar check karein ke "rabab" banta hai ya nahi.
def reverse_message(text):
    if len(text) <= 1:
        return text
    return reverse_message(text[1:]) + text[0]
print(reverse_message("Babar"))

# QUESTION 5: Corona Virus Double Spread (Recursive Power)
# Ek lab mein virus har ghante mein double (2x) ho jata hai.
# Hamein N ghante baad virus ki taqat nikalni hai (yani 2 ki power N).
# `def virus_spread(hours)` naam ka ek recursive function banayein.
# Base Case: 0 ghante par taqat 1 hoti hai (2^0 = 1).
# Recursive Case: 2 ko multiply karein `virus_spread(hours - 1)` se.
# Check karein ke 5 ghante baad virus kitna taqatwar hota hai.
def virus_spread(hours):
    if hours == 0:
        return 1
    return 2 * virus_spread(hours - 1)
print(virus_spread(5))

# QUESTION 6: The Delivery Box Flattener (Nested List Flattening)
# Ek khichdi delivery box aya hai jisme dabba ke andar dabba hai:
# boxes = ["Burger", ["Fries", "Nuggets"], "Chai"]
# Ghaur se dekhein, andar ek aur list mojud hai.
# `def flatten_boxes(items)` naam ka ek recursive function banayein.
# Ek naye khali list banayein. Loop chalayein: agar item khud ek list hai,
# to is function ko dobara call karein, warna aam item ko append karein.
# Aakhir mein ek saaf suthri single list return karein bina kisi nesting ke.
def flatten_boxes(items):
    flat_list = []
    
    for item in items:
        # Agar item khud ek list (dabba) hai
        if type(item) == list:
            # Recursion ka jadu: us andar wale dabbe ko kholo
            flat_list.extend(flatten_boxes(item))
        else:
            # Agar aam khana hai to seedha list mein daal do
            flat_list.append(item)
            
    return flat_list

boxes = ["Burger", ["Fries", "Nuggets"], "Chai"]
clean_menu = flatten_boxes(boxes)
print("Saaf suthra single khane ka menu:", clean_menu)