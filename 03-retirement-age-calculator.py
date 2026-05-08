#  Write a program that prompts the user for their age and tells them how many years until they reach retirement age (65).
a=int(input("Enter your age:"))
if a<=65:
    print("The age of Person is:",a)
    age_left=65-a
    print("The no. of years they have until they attain 65 years is:",age_left)
else:
    print("They have already attained 65.")

print("*****************************************")    



