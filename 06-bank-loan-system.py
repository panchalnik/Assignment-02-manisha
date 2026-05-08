# You have to create a javascript script that checks whether an user is eligible for a bank loan based on various criteria.
a=int(input("Enter Applicant's Age :"))
b=int(input("Enter Applicant' monthly income:"))
c=int(input("Enter applicant's credit score:"))
d=int(input("Enter applicant's outstanding debt:"))
if a>=18 and a<=60:
    print("cleared age criterion")
    if b>=25000:
        print("cleared income criterion")
        if c>=700:
            print("cleared credit score criterion")
            if d<=10000:
                print("Congratulations You are Eligible for loan")

else:
    print("You are not eligible for loan hence loan rejected")