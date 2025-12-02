# vending Machine notes
# the vending program works best by using three main tools:
# Dictionary: the mutable data storage, like inventory, menu, price, item no..
# List: mutable collection of items, like shopping cart, selected items.
# While loop:  used for iteration. asks user’s input indefinitely until a specific exit condition (break) is met.
#For Loop: data interation. it runs a fixed num (once for each item) to read the menu and print the list.
# skipped tools like multiple individual variables, instead of a dictionary to make the code much shorter, esp if you had 100 items?
#1. Bullet Points 1 & 3 -  1. Build a program that: 3. Asks the user to choose items by number in a loop.
def vending_machine(): # () is to def a f(x). Other f(x) are ‘print’, ‘input’, ‘tuple (immutable list)’
    inventory = {
        # #Inventory: A dictionary for item lookup (Item Number -> Details)
        # Structure: 'Outer Key' (String '1') maps to { 'Inner Key' (String 'name' 'price'): Inner Value (String/Float) 'chips, 1.75 }
        '1': {'name': 'Soda', 'price': 2.50},
        '2': {'name': 'Chips', 'price': 1.75},
        '3': {'name': 'Water', 'price': 1.00},
        '4': {'name': 'Candy Bar', 'price': 1.50},
    }
    selected_items = []  # [] is List to store shopping cart items
    total_cost = 0.0     # 'total_cost' is our variable. The register is @ 0.0 cos its empty & also a Float
    # --- DISPLAY MENU (SIMPLE DEFAULT) --- (bullet point 1)
    print("\n--- Welcome to the Vending Machine! ---")
    print("Available Items:")
    print("---------------------------------")  #the num of --- here is insignificant but helps with visual formatting
    for num, item_info in inventory.items():   ## Unpacks the key ('num') and value ('item_info') in each loop iteration.
        # # #ADVANCED NOTE: Use the line below for column alignment and pipes:
        # # # print(f"| {num}: {item_info['name']:<10} | ${item_info['price']:.2f} |")
        # the SIMPLER version:
        # for loop -to make ‘num’ = '1', AND item_info {'name': 'Soda', 'price': 2.50},
        print(f"Item {num}: {item_info['name']} - ${item_info['price']:.2f}")
    print("---------------------------------")
    print("Type the item number to select, or 'done' to finish.\n")
    # --- SELECTION LOOP (bulllets 2, 3, & 4) ---
    while True: #while loop creates infinite loops so used for breaks
        choice = input("Enter your selection: ").strip().lower()
                                            # .strip() - removes any hidden whitespace (spaces, tabs, new lines) in case of errs
                                            #.lower() - removes case sensitivity to 'Done'
        if choice == 'done': #econdition for Exit loop
            break
        if choice in inventory:  # Checks if the input is a valid item number.
            item_data = inventory[choice]
            #for bullet point 3 Asks the user to choose items by number in a loop.
            selected_items.append(item_data) ## Adds item data to the list.
            total_cost += item_data['price'] ## # Adds the price to the running total.
            print(f":white_check_mark: Added {item_data['name']}. Current Total: ${total_cost:.2f}")
        else:
            print(f":x: Invalid selection. Please enter a valid item number or 'done'.")
    # --- PRINT RECEIPT (bullet point 5) ---
    print("\n\n=============================================")
    print(":receipt: Here Is Your Final Receipt")
    if not selected_items:
        print("No items purchased. Thank you!")
    else:
        print("Items Purchased:")
        ## List of selected items with prices
        for item in selected_items:
            # Using simple formatting on the receipt.  Prints the name and price for each item in the list.
            print(f"- {item['name']}: ${item['price']:.2f}")
        print("---------------------------------------------")
        print(f"**TOTAL COST: ${total_cost:.2f}**")   # Prints the final accumulated Total Cost.
    print("=============================================")
if __name__ == "__main__":
    vending_machine()



















