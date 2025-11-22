
#Simple Grocery Cart Checkout Write a program that:
# Has a predefined dictionary of groceries with prices.
# Lets the user “add” items by typing their names.
# For each valid item, asks for the quantity. Keeps adding to the cart until the user types "checkout".
# Displays a final bill: each item, quantity, subtotal, and total. Skills practiced: dictionaries,
# loops, input(), math operations, formatting, error handling. help me solve easly way
# step1 Create a dictionary of items with prices, Create an empty cart, Ask user to type item names in a loop,
# then After checkout → print bill

groceries = {
    "apple": 10.0,
    "turkey": 11.0,
    "potatoes": 5.0,
    "flour": 2.5
}

cart = {}

print("Available items:")
for item, price in groceries.items():
    print(f"- {item}: ${price}")

while True:
    user_item = input("\nEnter item name (or type 'checkout'): ").strip().lower()

    if user_item == "checkout":
        break

    # check if item exists
    if user_item not in groceries:
        print("❌ Item not found. Try again.")
        continue

    # ask quantity
    try:
        qty = int(input("Enter quantity: "))
    except ValueError:
        print("❌ Please enter a valid number.")
        continue

    # add to cart
    if user_item in cart:
        cart[user_item] += qty
    else:
        cart[user_item] = qty

print("\n🧾 FINAL BILL")
print("-----------------------")

total = 0

for item, qty in cart.items():
    price = groceries[item]
    subtotal = price * qty
    total += subtotal
    print(f"{item} x {qty} = ${subtotal:.2f}")

print("-----------------------")
print(f"TOTAL = ${total:.2f}")

