#Write a Python program that iterates over a list of passwords. If the password meets certain criteria (e.g.,
# length greater than 8 characters, contains at least one digit, contains at least one special character),
# print "Strong password". Otherwise, do nothing (use the pass statement)

passwords = ["abc123", "password123", "secureP@ssw0rd", "weak"]
for password in passwords:
    if len(password) >= 8 and any(char.isdigit() for char in password) and any(char in "!@#$%^&*()" for char in password):
        print("Strong password")
    else:
        pass
