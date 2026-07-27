# =====================================================================
# TOPIC: PYDANTIC (Data Validation, BaseModel, Fields & Custom Validators)
# TOTAL QUESTIONS: 6 (1 Easy, 2 Medium, 3 Hard)
# INSTRUCTIONS: Write your Python code below each comment block.
# =====================================================================

# Hint: Pydantic v2 ke tools import karein
from pydantic import BaseModel, Field, ValidationError, field_validator
from typing import List, Optional

# ---------------------------------------------------------------------
# 🟢 EASY LEVEL
# ---------------------------------------------------------------------

# QUESTION 1: The University Admission Guard (Basic BaseModel)
# `BaseModel` se inherit kar ke `StudentModel` naam ki class banayein.
# Isme teen fields typed honi chahiye:
# name (str), roll_no (int), aur gpa (float).
# Baahir ek sahi data ka dictionary banayein aur `StudentModel(**data)` 
# likh kar validate karein. Phir use print kar ke check karein.
from pydantic import BaseModel, Field, ValidationError, field_validator
from typing import List, Optional
class StudentModel(BaseModel):
    name : str
    roll : int
    gpa : float
data = {"name" : "Babar" , "roll" : 49 , "gpa" : 3.56}
s1 = StudentModel(**data)
print("Name = " , s1.name)
print("Roll = " , s1.roll)
print("Gpa" , s1.gpa)

# ---------------------------------------------------------------------
# 🟡 MEDIUM LEVEL
# ---------------------------------------------------------------------

# QUESTION 2: Canteen Inventory Setup (Defaults & Optional Fields)
# Ek model banayein `CanteenItem`. Fields ye honi chahiye:
# 1. item_name (str) -> Lazmi field hai.
# 2. price (int) -> Lazmi field hai.
# 3. description (Optional[str]) -> Yeh optional ho aur default value None ho.
# 4. tax_included (bool) -> Iski default value True set karein.
# Baahir sirf item_name aur price de kar object banayein aur defaults check karein.
from pydantic import BaseModel, Field, ValidationError, field_validator
from typing import List, Optional
class CanteenItem(BaseModel):
    name : str
    price : int
    desc : Optional[str] = None
    tax : bool = True
obj1 = CanteenItem(name = "Samose" , price = 20)
print(f"OBJ 1.. , Name = {obj1.name} , Price = {obj1.price} , Description = {obj1.desc} , tax = {obj1.tax}")
obj2 = CanteenItem(name = "Sause" , price = 290)
print(f"OBJ 1.. , Name = {obj2.name} , Price = {obj2.price} , Description = {obj2.desc} , tax = {obj2.tax}")

# QUESTION 3: Secure Sign-up Form Validation (Using Field())
# Pydantic ka `Field` tool advanced rules lagane ke liye hota hai.
# Ek model banayein `UserSignup`.
# 1. username (str) -> Isme shart lagayein ke lambai kam az kam 5 ho (min_length=5).
# 2. age (int) -> Isme shart lagayein ke age 18 se bari ya barabar ho (ge=18).
# Hint: Field(..., min_length=5) aur Field(..., ge=18) ka use karein.
from pydantic import BaseModel, Field, ValidationError, field_validator
from typing import List, Optional
class UserSignup(BaseModel):
    user_name : str = Field(...,min_length = 5)
    age : int = Field(...,ge = 18)
obj1 = UserSignup(user_name = "Babar", age= 20)
print("Name = " , obj1.age , " , Age = " , obj1.age)
obj2 = UserSignup(user_name = "Babar", age= 20)
print("Name = " , obj2.age , " , Age = " , obj2.age)
obj3 = UserSignup(user_name = "Babar", age= 20)
print("Name = " , obj3.age , " , Age = " , obj3.age)

# ---------------------------------------------------------------------
# 🔴 HARD LEVEL
# ---------------------------------------------------------------------

# QUESTION 4: Safe API Crash Controller (Catching ValidationError)
# Jab Pydantic ko galat data milta hai, to wo `ValidationError` deta hai.
# Q1 mein banaye gaye `StudentModel` ka use karein.
# Ek galat data ka dictionary banayein: `faulty_data = {"name": "Babar", "roll_no": "Ten", "gpa": 3.8}`
# Ghaur se dekhein, roll_no mein int ki bajaye text "Ten" likha hai.
# Isay try-except block mein daal kar `ValidationError` ko pakrein aur `.json()` error print karein.
from pydantic import BaseModel, Field, ValidationError, field_validator
from typing import List, Optional
import json
class StudentModel(BaseModel):
    name : str
    roll : int
    gpa : float
data = {"name": "Babar", "roll_no": "Ten", "gpa": 3.8}
try : 
    s1 = StudentModel(**data)
    print("Name = " , s1.name)
    print("Roll = " , s1.roll)
    print("Gpa" , s1.gpa)
except ValidationError as ve:
    print("Something goes wrong..")
    print("Error = " , ve.json())
    print("Error class = " , ve.__class__.__name__)

# QUESTION 5: University Merit Controller (Custom @field_validator)
# Hamein check karna hai ke koi bacha galti se 4.0 se zyada GPA na likh de.
# `StudentModel` jaisa model banayein, lekin gpa field ke liye ek custom
# validator function banayein jis ke oopar `@field_validator('gpa')` laga ho.
# Andar check karein: Agar value 4.0 se bari (> 4.0) hai, to `ValueError`
# raise karein: "GPA limit se baahir hai!". Baahir 4.5 GPA de kar test karein.
from pydantic import BaseModel, Field, ValidationError, field_validator
from typing import List, Optional
class StudentModel(BaseModel):
    name : str
    roll : int
    gpa : float 
    @field_validator('gpa')
    def check_gpa(cls, v):
        if v > 4.0:
            raise ValueError("Jnb gpa kabhi b 4.0 say zyada nahi ho skta.")
        return v

data = {"name": "Babar", "roll": 10 , "gpa": 3.0}
try : 
    s1 = StudentModel(**data)
    print("Name = " , s1.name)
    print("Roll = " , s1.roll)
    print("Gpa" , s1.gpa)
except ValidationError as ve:
    print("Something goes wrong..")
    print("Error = " , ve.json())
    print("Error class = " , ve.__class__.__name__)

# QUESTION 6: Data Science Project Team (Nested Models Structure)
# Data science mein data nested hota hai (dabba ke andar dabba).
# 1. Pehle ek chota model banayein `TeamMember` jisme name (str) aur role (str) ho.
# 2. Phir ek bada model banayein `ProjectGroup` jisme project_name (str) aur 
#    members ki ek poori list ho, jiski type `List[TeamMember]` ho.
# Baahir ek nested dictionary (Group name aur 2 members ka data) bana kar 
# baday model se validate karayein aur screen par show karein.
from pydantic import BaseModel, Field, ValidationError, field_validator
from typing import List, Optional
class TeamMember(BaseModel):
    name : str 
    role : str
class ProjectGroup(BaseModel):
    project_name : str
    members : List[TeamMember]
group_payload = {
    "project_name": "SLAF Management System",
    "members": [
        {"name": "Babar Khan", "role": "Leader"},
        {"name": "Arshma Afzal", "role": "Developer"}
    ]
}
obj = ProjectGroup(**group_payload)
print("Project Name = " , obj.project_name)
print("Members = " , obj.members)