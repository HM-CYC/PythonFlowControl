#: Write a Python program that categorizes a student's grade based on their exam score.
# If the score is above 90, print "A". If it's between 80 and 90, print "B". If it's between 70 and 80,
# print "C". If it's between 60 and 70, print "D". Otherwise, print "F".

score = int(input("Enter your exam score: "))
if score > 100 :
    print("not within score range")
elif score < 0:
    print("error")
elif score > 90:
    print("A")
elif score > 80:
    print("B")
elif score > 70:
    print("C")
elif score > 60:
    print("D")
else:
    print("F")
