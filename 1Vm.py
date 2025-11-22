# 1. Vending Machine Program
# Build a program that:
# Displays a list of snacks and drinks with item numbers and prices.
# Asks the user to choose items by number in a loop.
# Keeps track of selected items and their prices.
# Ends when the user types “done”.
# Finally prints a receipt showing:
# List of selected items with prices
# Total cost
# Skills practiced: loops, input(), conditionals, lists/dictionaries, sum(), print formatting


def selected_items_price(order, amount):
    # order is a tuple like ('chips', 2)
    selected_item_name = order[0]
    selected_item_value = order[1]
    update = selected_item_value * amount
    updated = f"the price of {amount} {selected_item_name} is {update}"
    return update, updated

Items = {
    1: ('chips', 2),
    2: ('fruit', 5),
    3: ('peanut', 3),
    4: ('Chocolate Chip', 6),
    5: ('Blueberry Crisp', 6),
    6: ('water', 2),
    7: ('iced tea', 1),
    8: ('cold coffee', 3),
    9: ('Energy drink', 6),
}

# print available items nicely
print("Available Items:")
for key, val in Items.items():
    print(f"{key}: {val[0]} - {val[1]}")


order_list = []
total_amount = 0

while True:
    req = input("enter item number or write done: ").strip()
    if req.lower() == 'done':
        break

    # basic validation: must be a digit and a valid item number
    if not req.isdigit() or int(req) not in Items:
        print("Invalid item number. Please try again.")
        continue

    item = Items[int(req)]

    amount = input(f"how many {item[0]} do you want? ").strip()
    if not amount.isdigit() or int(amount) < 1:
        print("Invalid amount. Please enter a positive number.")
        continue

    amount = int(amount)

    # call the function to calculate price and get the message
    line_price, message = selected_items_price(item, amount)
    print(message)

    # store the order line and add to total
    order_list.append((item[0], item[1], amount, line_price))
    total_amount += line_price

# print a simple receipt
print("\n----- Receipt -----")
if not order_list:
    print("No items purchased.")
else:
    for name, unit_price, qty, subtotal in order_list:
        print(f"{name}  x{qty}  @ {unit_price} each  ->  {subtotal}")
    print("-------------------")
    print(f"Total: {total_amount}")
print("-------------------")