fruites_and_prices = {
    'banana': 12.48,
    'apple': 9.00,
    'kiwi': 13.00,
    'mango': 14.00,
    'grapes': 6.07,
    'oranges': 45.23,
    'peaches': 54.00,
    'plums': 24.21,
    }



def fruit_query():
    """Queries the price of fruit."""

    active_fruite_query = True

    while active_fruite_query:
        fruit = input("\nWhich fruit would you like to know the price of ?" +
        "\nYou can also exit by typing 'quit'." +
        "\nOr get a list of available fruit by typing 'list'.\n:")

        if fruit.lower() in fruites_and_prices:
            print("\nThe price of a " + fruit.lower() +
             " is R" + str(fruites_and_prices[fruit.lower()]))

        elif fruit.lower() == 'quit':
            break

        elif fruit.lower() == 'list':
            print("\n")
            for fruit in fruites_and_prices:
                 print(fruit.title())

        else:
            print("\nSorry we do not have '" + fruit.lower() +
            "'.\nHere is a list of our available fruit:\n")

            for fruit in fruites_and_prices:
                print(fruit.title())

        exit_message = ("\nIf you would like to look up " +
        "the price of a different fruit press Enter." +
        "\nTo Exit type 'quit' to exit.\n: ")

        exit = input(exit_message)

        if exit.lower() == 'quit':
            active_fruite_query = False

    return fruites_and_prices[fruit.lower()]


def fruit_price_update():
    """Updates the prices in the dictionary."""

    active = True
    while active:
        fruit_change = input("\nWhich fruit would you like to change the price of ?"+
        "\nType exit to exit." + "\n: ")

        if fruit_change.lower() in fruites_and_prices:
            print("\nYou may change the price of " + fruit_change.title() + "'s")

            try:
                new_price = int(input("\nWhat would you like the new price to be ?\n: "))

            except ValueError:
                print("You did not in put a numerical value!")
                continue

            confirmation = input("Are you sure you want to change the price of " +
            fruit_change.title() + " to R" + str(new_price) + " ?" +
            "\nType Yes to confirm, Type anything else to exit.\n: ")

            if confirmation.lower() == 'yes':
                fruites_and_prices[fruit_change] = new_price
                print("The new price of " + fruit_change +
                " is " + str(new_price))
                print(fruites_and_prices)
            else:
                break


        elif fruit_change == 'exit':
            break
        else:
            print("\nSorry that fruit is not in the list!" +
            "\nChoose another fruit.")

def stock_price_total():
    """Calculates the total of all the values in fruites_and_prices."""

    total_stock_price = 0

    for price in fruites_and_prices.values():
        stock_price = price
        total_stock_price += stock_price

    print("The total stock value for all items is R" + str(total_stock_price))

def check_out(customer_trolly):
    """Calculates the final checkout price,
       As well as lists the items that have been bought.
    """
    checkout_price = 0

    print("\nItems in checkout:")

    for item in customer_trolly:
        print(item.title() +"'s R" + str(fruites_and_prices[item.lower()]))

    for item in customer_trolly:

        price = fruites_and_prices[item.lower()]
        checkout_price += price
    print("\nThe total cost of purchase: R" + str(checkout_price))
    print("\nThank you for shopping at 7-11!")

granny = ['mango', 'banana']

check_out(granny)
