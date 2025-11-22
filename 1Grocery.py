# Simple Grocery Cart Checkout (fixed and improved)

item_price_usd = {
    'Eggs_dozen': 0.4,
    'Milk_galen': 4.45,
    'Chicken_1_lb': 6.99,
    'Ground_Beef_1_lb': 6.83,
    'Bread_1_lb': 3.06,
    'Potatoes_5_lb': 2.93,         # removed accidental trailing space in key
    'Cereal_12_oz': 3.27,
    'Tuna_5_oz_can': 1.14,
    'Pasta_Sauce_24_oz_jar': 2.62,
    'Bananas_Per_lb': 0.67
}

# Print menu
print("Item Name\t\t\tPrice (USD)")
print("-" * 40)
for k, v in item_price_usd.items():
    print(f"{k:<25}  ${v:>6.2f}")
print("-" * 40)
print("Type the item name to add it to your cart. Type 'checkout' to finish.\n")

# Build a case-insensitive lookup: normalized -> canonical key
def normalize(s: str) -> str:
    return s.strip().lower()

lookup = { normalize(k): k for k in item_price_usd.keys() }

cart_items = {}  # canonical_item_name -> quantity (int)

while True:
    order_raw = input("Write name of the item (or 'checkout'): ").strip()
    order_norm = normalize(order_raw)

    if order_norm == 'checkout':
        # checkout flow
        if not cart_items:
            print("Your cart is empty. See you another time!")
        break

    # check if item exists (case-insensitive)
    if order_norm not in lookup:
        print("Item not found. Please type an item name exactly as shown in the menu (case-insensitive).")
        continue

    canonical_name = lookup[order_norm]

    # get quantity
    while True:
        quant_raw = input(f"How many '{canonical_name}' do you want? ")
        try:
            qty = int(quant_raw)
            if qty <= 0:
                print("Please enter a positive whole number for quantity.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a whole number (e.g., 1, 2, 3).")

    # add to cart (accumulate if already present)
    previous = cart_items.get(canonical_name, 0)
    cart_items[canonical_name] = previous + qty
    print(f"Added {qty} x {canonical_name} to cart. (Now {cart_items[canonical_name]} total)\n")

# Print final bill
def print_bill(cart: dict, prices: dict):
    if not cart:
        print("No items to bill.")
        return

    print("\nFinal Bill")
    print("-" * 60)
    print(f"{'Item':<30}{'Qty':>6}{'Unit':>12}{'Subtotal':>12}")
    print("-" * 60)
    total = 0.0
    for item, qty in cart.items():
        unit_price = prices[item]
        subtotal = unit_price * qty
        total += subtotal
        # formatting
        print(f"{item:<30}{qty:>6}{unit_price:>12.2f}{subtotal:>12.2f}")
    print("-" * 60)
    print(f"{'TOTAL':<30}{'':>6}{'':>12}{total:>12.2f}")
    print("-" * 60)

print_bill(cart_items, item_price_usd)



