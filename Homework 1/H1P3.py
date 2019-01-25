pennies = int(input("How many pennies do you have?: "))
nickels = int(input("How many nickels do you have?: "))
dimes = int(input("How many dimes do you have?: "))
quarters = int(input("How many quarters do you have?: "))
half_dollars = int(input("How many half dollars do you have?: "))
dollar_coins = int(input("How many dollar coins do you have?: "))
cents = float(pennies + (nickels * 5) + (dimes * 10) + (quarters * 25) + (half_dollars * 50) + (dollar_coins * 100))
total = float(cents / 100)

#used https://stackoverflow.com/questions/22599540/plurals-if-statement-python for help with the plural if statements
print("You have " + str(pennies) + (" penny." if pennies == 1 else " pennies") + "\nYou have " + str(nickels) + (" nickel." if nickels == 1 else " nickels.") + "\nYou have " + str(dimes) + (" dime." if dimes == 1 else " dimes.") + "\nYou have " + str(quarters) +(" quarter." if quarters == 1 else " quarters.") + "\nYou have " + str(half_dollars) + (" half dollar." if half_dollars == 1 else " half dollars.") + "\nYou have " + str(dollar_coins) + (" dollar coin." if dollar_coins == 1 else " dollar coins.") + "\nYour total is $" + str(total))