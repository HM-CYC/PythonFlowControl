# Write a Python program that checks if a person is eligible for a driver's license. If the person is above 18 years old,
# check if they have a learner's permit. If they have a learner's permit, print "Eligible for license". If not, print
# "Not eligible for license

age = int(input("Enter your age: "))
has_permit = input("Do you have a learner's permit? (yes/no): ")

if age >= 18:
    if has_permit.lower() == "yes":
        print("Eligible for license")
    else:
        print("Not eligible for license")
else:
    print("Not eligible for license")
