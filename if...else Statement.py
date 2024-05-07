#Write a Python program that checks if a given number is a prime number or not. If it's prime, print "Prime",
# otherwise print "Not Prime".
num = int(input("Enter a number: "))
is_prime = True

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
else:
    is_prime = False

if is_prime:
    print("Prime")
else:
    print("Not Prime")
