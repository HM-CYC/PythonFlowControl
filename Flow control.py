# if statement and if elif , else
x = int(input("Enter a number: "))
if x > 5: # الشرط
    print("x is greater than 5")

y = int(input("Enter another number: "))
if y % 2 == 0: #الشرط الاول
    print("y is even")
else: #الشرط الثاني
    print("y is odd")

z = int(input("Enter one more number: "))
if z > 0: #الشرط
    print("z is positive")
elif z == 0: #الشرط المحتمل
    print("z is zero")
else: #الشرط الاخير
    print("z is negative")


# Python for Loop m while loop

numbers = [1, 2, 3, 4, 5]

print("Python for Loop")
for number in numbers:
    print(number)
print()

print("Python for Loop with Range")
for i in range(1, 11):
    print(i)
print()

message = "Hello, World!"
print(" Python for Loop with Strings")
for char in message:
    print(char)
print()

print("Python while Loop")
count = 5
while count > 0:
    print(count)
    count -= 1
print()

print("Python while Loop with User Input")
total = 0
number = 1

while number != 0:
    number = int(input("Enter a number (enter 0 to stop): "))
    total += number

print("Sum of numbers entered:", total)

