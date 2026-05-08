# Write a program that takes input for the cost price and selling price of an item.
cost_price=int(input("Enter the cost price of item:"))
selling_price=int(input("Enter the selling price of item:"))
profit=selling_price-cost_price
loss=cost_price-selling_price

if selling_price>cost_price:
    print("The respective profit is :", profit)
    profit_percentage=(profit/cost_price)*100
    print(f"The respective profit percentage is",{profit_percentage})
else:
    print("The respective loss is :",loss)
    loss_percentage=(loss/cost_price)*100
    print("The respective loss percentage is:",loss_percentage)

print("😊😊😊😊😊😊😊😊😊😊😊")    
