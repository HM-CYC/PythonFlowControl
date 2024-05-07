#Write a Python program that simulates network access control using a loop to repeatedly prompt the user for
# credentials until authentication is successful

valid_username = "admin"
valid_password = "123456"
while True:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == valid_username and password == valid_password:
        print("Authentication successful. Access granted.")
        break
    else:
        print("Authentication failed. Please try again.")


