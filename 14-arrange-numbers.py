# Write a javascript program to arrange three numbers in descending order.

a=int(input("Enter your first number:"))
b=int(input("Enter your second number:"))
c=int(input("Enter your third number:"))
# if a<b and a<c:
#     print(f"smallest number is {a}")
# if b>a and b<c:
#     print(f"2nd largest and largest numbers are :{b} {c}")

# print(f"Therefore Numbers in decending orders are : {a} {b} and {c}")    


numbers=[a,b,c]
numbers.sort(reverse=True)

print("The numbers is decending order is",numbers)


numbers.sort(reverse=False)
print("The numbers in ascending order are",numbers)
