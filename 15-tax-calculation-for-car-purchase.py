# Write a program to calculate the tax on a car purchase based on the car brand and its price.

a=input("Enter the Brand of the Car:") 
b=int(input("Enter the price of the car in lakhs:"))

if b>=7 and b<10:
    tax_percentage=5
    tax=(b*tax_percentage)/100
    print(f"The calculated tax on this {a} in lakhs is {tax}")

if b>=10 and b<15:
    tax_percentage=10
    tax=(b*tax_percentage)/100
    print(f"The calculated tax on this {a} in lakhs is {tax} ")

if  b>=15 and b<20:
    tax_percentage=25
    tax=(b*tax_percentage)/100
    print(f"The calculated tax on this {a} in lakhs is {tax}")

if b>=20 and b<25:
    tax_percentage= 30
    tax=(b*tax_percentage)/100
    print(f"The calculated tax on this {a} in lakhs is {tax}")   

print("Congratulations for your new car")    

print("🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗")


