# Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit

def profit_loss_check():
    cost = float(input("Enter Cost Price: "))
    sell = float(input("Enter Selling Price: "))

    if sell > cost:
        profit = sell - cost
        print(f"You made a profit of: ${profit:.2f}")
    elif sell == cost:
        print("You sold at the same price as your cost. No profit, no loss.")
    else:
        loss = cost - sell
        print(f"You incurred a loss of: ${loss:.2f}")

profit_loss_check()
