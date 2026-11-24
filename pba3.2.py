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