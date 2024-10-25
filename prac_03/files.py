# 1.
# Open the file in write mode to save the user's name
# Using print makes it easy to write to the file and handle newlines
out_file = open("name.txt", "w")
name = input("What is your name? ")
print(name, file=out_file)
out_file.close()

# 2.
# Open the file in read mode and get the entire content as a single string
# We use read() here since we only need to read one line
in_file = open("name.txt", "r")
name = in_file.read().strip()  # Remove any extra whitespace
in_file.close()
print(f"Hi {name}!")

# 3.
# Open the file and read the first two lines separately
# readline() is used because we only need specific lines, not the entire file
with open("numbers.txt", "r") as in_file:
    number1 = int(in_file.readline())  # Convert the first line to an integer
    number2 = int(in_file.readline())  # Convert the second line to an integer
print(number1 + number2)  # Print the sum of the two numbers

# 4.
# Open the file and iterate over each line to calculate the total
# for line in file allows us to process each line independently
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        number = int(line)  # Convert each line to an integer
        total += number     # Add the number to the total
print(total)  # Print the total sum of all numbers
