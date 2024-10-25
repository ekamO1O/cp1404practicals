"""
Simulates daily stock price changes until it goes below $1 or above $100,
saving results to a file.
"""

import random

# Constants for customization
MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05   # 5%
MIN_PRICE = 1.0       # New minimum price
MAX_PRICE = 100.0     # New maximum price
INITIAL_PRICE = 10.0
FILENAME = "stock_simulation.txt"

# Initialize variables
price = INITIAL_PRICE
number_of_days = 0

# Open file for writing
out_file = open(FILENAME, 'w')

# Write the initial price
print(f"Starting price: ${price:,.2f}", file=out_file)

# Run the simulation
while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    number_of_days += 1

    # Decide whether the price goes up or down
    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)

# Close the file
out_file.close()
