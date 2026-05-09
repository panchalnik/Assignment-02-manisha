# Write a program to calculate the library charges based on the number of days a book has been borrowed.

a=int(input(" Enter the number of days the book has been borrowed:"))

if a<=5:
    print("The charges on the book is 2rupees per day")
elif 6<=a<=10:
    print("The charges on the book is 3rupees per day")  
elif 11<=a<=15:
    print("The charges on the book is 4rupees per day")      
elif a>=15:
    print("The charges on the book is 5rupees per day")    

print("------------------------------------------")    