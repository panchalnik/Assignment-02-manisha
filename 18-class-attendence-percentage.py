# Write a program to calculate the percentage of classes attended by a
# student and determine their eligibility to sit in the exam.


a=int(input("Percentage of class attended by student:"))

if a<75:
    print("Student is not allowed to sit in examination")
else:
    if a>=75:
       print("student is allowed to sit in examination")