"""CP1404 Practical, Warm-Up"""

numbers = [3, 1, 4, 1, 5, 9, 2]
#
# numbers[0]
# 3

# numbers[-1]
# 2

# numbers[3]
# 1

# numbers[:-1]
# [3, 1, 4, 1, 5, 9]

# numbers[3:4]
# [1]

# 5 in numbers
# True

# 7 in numbers
# False

# "3" in numbers
# False

# numbers + [6, 5, 3]
# [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]


# Task 1: Change the first element of numbers to "ten" (the string, not the number 10)
numbers[0] = "ten"

# Task 2: Change the last element of numbers to 1
numbers[-1] = 1

# Task 3: Print all elements from numbers except the first two (slice)
print(numbers[2:])

# Task 4: Print whether 9 is an element of numbers
print(9 in numbers)
