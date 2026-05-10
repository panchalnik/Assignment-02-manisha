# Create the Menu:T○ Display a menu with three choices for the user:
# ■ Login with Phone
# ■ Login with Email
# ■ Exit the system
# 2. Predefined Credentials:
#  Phone number: "1234567890"
#  OTP: "1234"
#  Email: "user@example.com"
#  Password: "password123”


a=int(input("Ask the user to Enter their Phone number:"))
b=int(input("Ask the user to Enter their OTP:"))

if a==1234567890 and b==1234:
    print("Login Successful with Phone !")
else:    
    print("OOPS, Invalid credentials")

c=(input("Enter your Email :"))
d=(input("Enter your Email password:"))

if c=="user@example.com" and d=="password123":
    print("Login Successful with Email !")

else:    
    print("OOPS, Invalid credentials")

user=input("exit the program:")
if user=="yes":
      print("Existing the Program,Have a nice day!")    