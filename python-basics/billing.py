def calculate_bill(price, qty):
    return price * qty
def pkr_to_usd(rupees):
    return rupees / 280
def welcome_admin(admin):
    print("Admin. Welcome to UOG , " , admin)
def welcome_student(std):
    print("Student. Welcome to UOG , " , std)
def count_presents(attendance_list):
    return attendance_list.count("Present")
def check_password(user):
    if user == "123":
        return True
    else:
        return False
def connect_db():
    print("Connecting ..")
if __name__ == "__user_modules_practice__":
    print("Running directly..")