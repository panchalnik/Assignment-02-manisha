# You will implement a javascript program to validate the domain of a user's email address. The program will check if the email contains a specific
# domain (e.g. "gmail.com").

a=input("Enter Your Email:")
find="gmail.com"
if (find in a) :
    print("Email is eligible for registration based on domain ")
else:
    print("Email is not eligible for Registration ")    