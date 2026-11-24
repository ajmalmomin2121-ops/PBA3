import re


def validate_password(password):
    if len(password) < 8:
        return False, "Must be at least 8 characters long"
    if not re.search(r"[A-Z]", password):
        return False, "Must contain an uppercase letter"
    if not re.search(r"\d", password):
        return False, "Must contain a digit"
    if not re.search(r"[^A-Za-z0-9]", password):
        return False, "Must contain a special character"
    return True, "Valid password"


for pwd in ["Pass@123", "pass123", "Admin#9"]:
    valid, msg = validate_password(pwd)
    print(f"{pwd} -> {msg}")

user_pwd = input("\nEnter a password: ")
valid, msg = validate_password(user_pwd)
print(msg)

output_______________________________________________

ajmal@ajmals-MacBook-Air / % /usr/local/bin/python3 /Users/ajmal/ajmal/ajmal.asm/pba3.2.py
Pass@123 -> Valid password
pass123 -> Must be at least 8 characters long
Admin#9 -> Must be at least 8 characters long

Enter a password: Pass@123
Valid password



