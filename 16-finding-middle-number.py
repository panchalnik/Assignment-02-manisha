# Task: Write a program to determine the middle number among three inputs.

a=int(input("Enter your first number:"))
b=int(input("Enter your second number:"))
c=int(input("Enter your Third number:"))
      
print(f"The three numbers are {a} {b} {c}")

if (a>=b and a<=c) or (a<=b and a>=c )  :
    print("Middle number is",a)
elif  (b>=a and b<=c) or (b<=a and b>=c) :
    print("Middle number is",b)
else:
    print("Middle number is ",c)
 

print("Congratulations You have found your middle number😊")    




