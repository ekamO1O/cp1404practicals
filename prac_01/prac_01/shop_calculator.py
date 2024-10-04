""" CALCULATOR """


# Shop Calculator

# Display menu
def display_menu():
    print("\nMenu:")
    print("1 - Calculate total price")
    print("2 - Quit")


# Get user choice
def get_choice():
    choice = input("Choose an option: ")
    return choice


# Calculate total price with discount if applicable
def calculate_total_price():
    # Input validation for number of items
    number_of_items = int(input("Number of items: "))
    while number_of_items < 0:
        print("Invalid number of items!")
        number_of_items = int(input("Number of items: "))

    total_price = 0
    for i in range(number_of_items):
        price = float(input(f"Price of item {i + 1}: "))
        total_price += price

    # Apply discount if total price is over $100
    if total_price > 100:
        discount = total_price * 0.10
        total_price -= discount

    # Print final total price
    print(f"Total price for {number_of_items} items is ${total_price:.2f}")


# Main program loop (using the while pattern as in the 2nd image)
display_menu()
choice = get_choice()

while choice != '2':  # '2' is the quit option
    if choice == '1':
        calculate_total_price()
    else:
        print("Invalid choice, please select 1 or 2.")

    # Re-display menu and get next choice
    display_menu()
    choice = get_choice()

print("Goodbye!")

