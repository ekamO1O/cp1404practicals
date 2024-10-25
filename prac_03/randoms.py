"""randoms.py"""


# What did you see on line 1?
# What was the smallest number you could have seen, what was the largest?

# 16
# Smallest Number: 5
# Largest Number: 20


# What did you see on line 2?
# What was the smallest number you could have seen, what was the largest?
# Could line 2 have produced a 4?

# 5
# Smallest Number: 3
# Largest Number: 9
# Possibility of 4: No, because randrange(3, 10, 2) steps by 2, producing only odd numbers (3, 5, 7, 9).


# What did you see on line 3?
# What was the smallest number you could have seen, what was the largest?

# 2.838264952996191
# Smallest Number: 2.5
# Largest Number: 5.5

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.

import random

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)
print(random_number)
