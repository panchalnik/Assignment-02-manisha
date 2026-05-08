# Write a javascript program that authenticates a user by checking their username and
# password. The program should compare the entered credentials with predefined valid credentials.""


a=input("Enter your username:")
b=input("Enter your Password:")
if a=="user1" and b=="pass@123":
    print("Authentication successful")
else:
    print("Authentication failed")
