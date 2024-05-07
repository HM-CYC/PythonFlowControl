#Write a Python program that calculates the factorial of a given number using a for loop. Print the factorial value at the end
num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("Factorial:", factorial)
