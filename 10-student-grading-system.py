# Create a javascript program to calculate a student's grade based on their marks.

a=int(input("Enter the marks of student:"))
if 90<=a<=100:
    print("grade a")
elif 80<=a<=89:
    print("grade B")
elif 70<=a<=79:
    print("Grade C")
elif 60<=a<=69:
    print("Grade D")
elif 50<=a<=59:
    print("Grade E")    
elif 0<=a<=49:  
    print("Grade F")

else:
    print("Invalid marks")



    