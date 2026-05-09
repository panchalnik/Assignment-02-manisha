# Write a program to find greatest number from three number

a=int(input("Enter your first number:"))
b=int(input("Enter your second number:"))
c=int(input("Enter your third number:"))

if a>=b and a>=c:
    print("The greatest number is",a)
if b>=a and b>=c:
    print("The greatest number is ",b)
if c>=a and c>=b:
    print("The greatest number is",c)        

print("congratulation your greatest number is found😊")    