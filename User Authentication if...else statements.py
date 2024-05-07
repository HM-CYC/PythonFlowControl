#Write a Python program to authenticate a user based on their username and password.

# اسماء الاعضاء في النظام و ترخيصاتهم
valid_username = "admin"
valid_password = "123456"
username = input("Enter username: ")
password = input("Enter password: ")
if username == valid_username and password == valid_password:
    print("Authentication successful. Access granted.")
else:
    print("Authentication failed. Access denied.")
