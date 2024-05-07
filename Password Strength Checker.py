#Write a Python program that checks the strength of a password and provides feedback to the user.

def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password should be at least 8 characters long."
    elif not any(char.isdigit() for char in password):
        return "Weak: Password should contain at least one digit."
    elif not any(char.isalpha() for char in password):
        return "Weak: Password should contain at least one letter."
    elif not any(char.isupper() for char in password):
        return "Weak: Password should contain at least one uppercase letter."
    elif not any(char.islower() for char in password):
        return "Weak: Password should contain at least one lowercase letter."
    else:
        return "Strong: Password meets all criteria."
password = input("Enter your password: ")
strength = check_password_strength(password)
print("Password Strength:", strength)
