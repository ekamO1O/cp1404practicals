"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

# Get the first sales input
sales = float(input("Enter sales: $"))

# Continue looping until the user enters a negative number
while sales >= 0:
    # Calculate bonus based on sales amount
    if sales < 1000:
        bonus = sales * 0.10  # 10% bonus
    else:
        bonus = sales * 0.15  # 15% bonus

    print(f"Bonus: ${bonus:.2f}")

    # Get the next sales input
    sales = float(input("Enter sales: $"))

# Program ends when a negative sales amount is entered
print("Program finished.")
