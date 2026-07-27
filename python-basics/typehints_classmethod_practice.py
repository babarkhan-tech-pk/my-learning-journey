# =====================================================================
# TOPIC: PYTHON TYPE HINTS AND CLASS METHODS (@classmethod)
# TOTAL QUESTIONS: 6 (1 Easy, 2 Medium, 3 Hard)
# INSTRUCTIONS: Write your Python code below each comment block.
# =====================================================================

# Hint: Type hints ke advanced tools ke liye typing module use karein
from typing import List, Dict, Optional

# ---------------------------------------------------------------------
# 🟢 EASY LEVEL
# ---------------------------------------------------------------------

# QUESTION 1: Secure Gate Welcome Note (Basic Type Hints)
# Ek saada function banayein `generate_welcome_note`.
# Type hints ka use kar ke batayein ke `name` ki type String (`str`) ho,
# aur `roll_no` ki type Integer (`int`) honi chahiye.
# Aur function ke end mein `-> str` lagayein jo bataye ke yeh function
# hamesha aik string hi return karega. Inside function, simple text return karein.
def generate_welcome_note(name : str , roll : int) -> str :
    return f"Hello {name} , Welcome. Roll no = {roll}"
print(generate_welcome_note("Babar",20))
print(generate_welcome_note("Ali",30))

# ---------------------------------------------------------------------
# 🟡 MEDIUM LEVEL
# ---------------------------------------------------------------------

# QUESTION 2: University Portal Rule Updater (@classmethod)
# Ek class banayein `UOGPortal`. Isme ek class attribute (variable) rakhein:
# `university_name = "University of Gujrat"`.
# `@classmethod` ka use kar ke ek method banayein `update_university(cls, new_name)`.
# Yeh method poori class ke liye university ka naam badal de.
# Baahir bina koi object banaye direct Class ke naam se isay call kar ke badlein.
class UOGPortal():
    university_name = "University of Gujrat"
    @classmethod
    def update_university(cls , new_name : str) -> None:
        cls.university_name = new_name
print(UOGPortal.university_name)
UOGPortal.update_university("Haiz Hayt Campus (UOG)")
print(UOGPortal.university_name)
UOGPortal.update_university("Haiz Hayt")
print(UOGPortal.university_name)


# QUESTION 3: Data Science Marks Evaluator (List & Dict Type Hints)
# Ek function banayein `calculate_average_marks(student_data)`.
# Type hints ka use kar ke batayein ke `student_data` darasl aik Dictionary hai
# jiske andar keys strings hain aur values integers ki list hain.
# Hint syntax: `student_data: Dict[str, List[int]]`
# Yeh function marks ka total average return (`-> float`) kare.
def calculate_average_marks(student_data : dict[str , list[int]]) -> float:
    all : list[int] = student_data["Marks"]
    total : int  = sum(all)
    avg : int = 0
    le : int = len(student_data)
    avg : int = total / le
    return float(avg)
std = {"Marks":[1,2,3,4,5]}
print(calculate_average_marks(std))

# ---------------------------------------------------------------------
# 🔴 HARD LEVEL
# ---------------------------------------------------------------------

# QUESTION 4: Smart Student Factory from String Payload
# Ek class banayein `Student` jisme constructor `__init__` name aur degree leta ho.
# Farz karein database ya web portal se data aik ajeeb string mein aa raha hai:
# `"Arshma-DataScience"` ya `"Zeeshan-DataScience"`.
# Class ke andar ek `@classmethod` banayein jis ka naam ho `from_string_payload(cls, text: str)`.
# Yeh method `.split("-")` ka use kar ke string ko alag karega, aur andar se hi 
# naya object tayaar (`return cls(name, degree)`) kar ke baahir thama dega!
class Student():
    def __init__(self , name : str , degree : str) -> None:
        self.name = name
        self.degree = degree
    @classmethod
    def from_string_payload(cls, text: str) -> object:
        name , degree = text.split("-")
        return cls(name , degree)
raw_data = "Arshma-DataScience"
student_obj = Student.from_string_payload(raw_data)
print(f"Object successfully created! Name: {student_obj.name}, Degree: {student_obj.degree}")


# QUESTION 5: Project Group Role Finder (The Optional Type Hint)
# Ek function banayein `find_member_role(members: List[str], target: str) -> Optional[str]`.
# Ghaur se dekhein, return type mein `Optional[str]` likha hai, iska matlab hai ke 
# function ya to string return karega (agar banda mil gaya) ya `None` (agar na mila).
# Loop chalayein, agar target mil jaye to "Developer" ya "Leader" return karein, warna None.
from typing import Optional
def find_member_roles(members : list[str] , target : str) -> Optional[str]:
    for m in members:
        if m == target:
            return "Developer"
        else:
            return None
mem = ["Babar", "Zeeshan"]
print(find_member_roles(mem,"Babar"))
print(find_member_roles(mem,"Ali"))

# QUESTION 6: Hybrid Group Batch Creator (Combining Class Method & Type Hints)
# Ek class banayein `ProjectGroup`. Constructor mein group ka name aur members ki list aaye.
# Is class ke andar ek typed class method banayein:
# `@classmethod`
# `def build_default_group(cls, group_name: str) -> "ProjectGroup":`
# Yeh method automatic teen core names `["Babar", "Arshma", "Nida"]` ki list banaye
# aur un bacho ke sath aik naya `ProjectGroup` ka object tayaar kar ke return kar de.
class ProjectGroup():
    def __init__(self , group_name : str , members : list[str]):
        self.group_name = group_name
        self.members = members
    @classmethod
    def build_default_group(cls, grp_name : str) -> "ProjectGroup":
        members = ["Babar" , "Arshma" , "Nida"]
        return cls(grp_name,members)
my_batch = ProjectGroup.build_default_group("SLAF Alpha Team")
print(f"Group: {my_batch.group_name} | Members inside: {my_batch.members}")
