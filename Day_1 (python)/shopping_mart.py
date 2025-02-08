# code should have list of items & their prices, from that list customer will select items
# code should be able to take items as input 
# code should be able to ask customer if they want to remove items from cart and take user input
# code should be able to exit if user press exit
# code should be able to delete items from the list
# code should be able to calculate total bill & items bought by customer

items = {
    # Staples
    "Cooking Oil (per litre)": 500,
    "Flour (per kg)": 250,
    "Rice (per kg)": 300,
    "Sugar (per kg)": 180,
    "Salt (per pack)": 50,

    # Dairy Products
    "Milk (per litre)": 250,
    "Cheese (per 200g)": 350,
    "Butter (per 250g)": 400,
    "Yogurt (per kg)": 180,
    "Eggs (per dozen)": 600,

    # Meat & Seafood
    "Chicken (per kg)": 700,
    "Beef (per kg)": 1200,
    "Mutton (per kg)": 1800,
    "Fish (per kg)": 1500,

    # Vegetables
    "Tomatoes (per kg)": 200,
    "Potatoes (per kg)": 150,
    "Onions (per kg)": 180,
    "Garlic (per kg)": 400,
    "Ginger (per kg)": 600,
    "Carrots (per kg)": 250,
    "Spinach (per bunch)": 80,

    # Fruits
    "Bananas (per dozen)": 250,
    "Apples (per kg)": 350,
    "Oranges (per dozen)": 500,
    "Mangoes (per kg)": 600,
    "Grapes (per kg)": 450,

    # Beverages
    "Tea (per 250g)": 400,
    "Coffee (per 100g)": 450,
    "Soft Drink (per 1.5L bottle)": 200,
    "Juice (per 1L pack)": 300,

    # Snacks
    "Biscuits (per pack)": 100,
    "Chips (per pack)": 80,
    "Chocolate (per bar)": 250,
    "Nuts (per 500g)": 800,

    # Household Essentials
    "Toothpaste (per tube)": 250,
    "Shampoo (per bottle)": 600,
    "Soap (per bar)": 180,
    "Dishwashing Liquid (per bottle)": 350,
    "Laundry Detergent (per kg)": 500,

    # Baby & Personal Care
    "Diapers (per pack)": 1500,
    "Baby Powder (per bottle)": 400,
    "Face Wash (per tube)": 350,
    "Lotion (per bottle)": 500,
    "Deodorant (per bottle)": 550
}
 

# Function to add items to the cart
def add_items_in_cart(items):
    cart = {}

    while True:
        item_name = input("Add items in your cart (or type 'exit' to finish): ").strip()

        if item_name.lower() == "exit":
            break

        if item_name in items:
            try:
                quantity = int(input("Quantity: "))
                if item_name in cart:
                    print("Item available, updating quantity.")
                    cart[item_name] += quantity
                else:
                    cart[item_name] = quantity
                print(f"{quantity} x {item_name} added to cart!")

                # Ask if the user wants to remove any item
                cart = delete_items(cart)

            except ValueError:
                print("Invalid quantity! Please enter a valid number.")
        else:
            print("Sorry! Item not available in the store.")

    return cart

def delete_items(cart):
    while True:
        remove_choice = input("Do you want to remove any item? (yes/no): ").strip().lower()

        if remove_choice == "no":
            return cart  # Immediately return to exit removal process

        elif remove_choice == "yes":
            item_name = input("Enter item to remove from cart: ").strip()

            if item_name in cart:
                try:
                    quantity = int(input("Enter quantity of item to remove: "))

                    if quantity >= cart[item_name]:  
                        del cart[item_name]  
                        print(f"{item_name} removed from cart.")
                    else:
                        cart[item_name] -= quantity  
                        print(f"{quantity} of {item_name} removed. Remaining: {cart[item_name]}")

                except ValueError:
                    print("Invalid input! Please enter a valid number.")
            else:
                print(f"{item_name} is not in your cart.")

        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def calculate_bill(cart, items):
    total_bill = 0
    print("\nYour Cart Summary:")
    for item, qty in cart.items():
        if item in items:
            item_total = qty * items[item]
            print(f"{item}: {qty} x Rs {items[item]} = Rs {item_total}")
            total_bill += item_total
        else:
            print(f"Error: {item} not found in price list.")

    print(f"\nTotal Bill: Rs {total_bill}")
    return total_bill

cart = add_items_in_cart(items)
calculate_bill(cart, items)