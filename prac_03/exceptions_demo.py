"""exceptions_demo.py"""

# When will a ValueError occur?

# A ValueError will occur if the user inputs something that cannot be converted to an integer
# (e.g., letters or special characters). This error happens when int(input(...)) fails due to invalid input.


# When will a ZeroDivisionError occur?

# A ZeroDivisionError will occur if the user inputs 0 for the denominator.
# Dividing by zero is not allowed in Python, hence the error.


# How to avoid a ZeroDivisionError?

# You can avoid a ZeroDivisionError by checking if
# the denominator is zero before performing the division.

# Here’s how you can modify the code to handle this:

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
