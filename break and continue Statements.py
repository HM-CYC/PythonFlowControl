#Write a Python program that iterates over a list of numbers. If the number is even, print it.
# If the number is odd, skip it and continue to the next number. Use the continue statement
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num % 2 != 0:
        continue
    print(num)
