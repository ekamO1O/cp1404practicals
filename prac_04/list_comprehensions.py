"""CP1404 Practical, List comprehensions"""

names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing", "Ada Lovelace"]

# For loop that creates a new list containing the first letter of each name
first_initials = []
for name in names:
    first_initials.append(name[0])
print(first_initials)

# List comprehension that does the same thing as the loop above
first_initials = [name[0] for name in names]
print(first_initials)

# List comprehension that creates a list containing the initials
# Splits each name and adds the first letters of each part to a string
full_initials = [name.split()[0][0] + name.split()[1][0] for name in full_names]
print(full_initials)

# Filtering to select only the names that start with 'A'
a_names = [name for name in names if name.startswith('A')]
print(a_names)

# Create a list of all of the full_names in lowercase format
lowercase_full_names = [name.lower() for name in full_names]
print(lowercase_full_names)

# Almost numbers as strings
almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']
# Create a list of integers from the above list of strings
numbers = [int(almost_number) for almost_number in almost_numbers]
print(numbers)

# Create a list of only the numbers that are greater than 9
big_numbers = [number for number in numbers if number > 9]
print(big_numbers)

# Create a string of the last names for full names longer than 11 characters
last_names = ', '.join([name.split()[1] for name in full_names if len(name) > 11])
print(last_names)
