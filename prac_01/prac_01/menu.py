"""menus.py"""

# Get the user's name
name = input("Enter name: ")


# Function to display the menu
def display_menu():
    print("\n(H)ello")
    print("(G)oodbye")
    print("(Q)uit")


# Display the menu for the first time
display_menu()

# Get the user's choice
choice = input(">>> ").upper()

# Loop until the user chooses to quit
while choice != 'Q':
    if choice == 'H':
        print(f"Hello {name}")
    elif choice == 'G':
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")

    # Display the menu again
    display_menu()

    # Get the user's choice again
    choice = input(">>> ").upper()

# Display the finished message once the loop ends
print("Finished.")
