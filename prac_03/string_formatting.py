"""Format the Guitar Information"""

year = 1922
name = "Gibson L-5 CES"
cost = 16035.9

# Using f-string formatting to include variables in the string
print(f"{year} {name} for about ${cost:,.0f}!")


"""Print Powers of 2 in a Right-Aligned Format"""

# Using a for loop to generate powers of 2 and right-align the output
for i in range(11):
    print(f"2 ^ {i:<2} is {2 ** i:>4}")
