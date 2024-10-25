"""CP1404 Practical, "Quick Pick" Lottery Ticket Generator"""


import random

# Constants for the number of picks and the range of lottery numbers
NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    """Generate random lottery numbers."""
    number_of_quick_picks = int(input("How many quick picks? "))
    while number_of_quick_picks < 0:
        print("That makes no sense!")
        number_of_quick_picks = int(input("How many quick picks? "))

    # Generate and print the specified number of unique quick picks
    for i in range(number_of_quick_picks):
        quick_pick = []  # List to store numbers for the current quick pick

        # Fill the quick pick with unique random numbers
        while len(quick_pick) < NUMBERS_PER_LINE:
            number = random.randint(MINIMUM, MAXIMUM)
            if number not in quick_pick:  # Ensure no duplicates
                quick_pick.append(number)

        quick_pick.sort()  # Sort the numbers in ascending order
        print(" ".join(f"{number:2}" for number in quick_pick))  # Print formatted quick pick


# Execute the main function when the script runs
main()
