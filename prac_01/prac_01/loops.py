"""LOOPS"""

# a. Count in 10s from 0 to 100
print("a. Count in 10s from 0 to 100:")
for i in range(0, 101, 10):
    print(i, end=' ')
print("\n")

# b. Countdown from 20 to 1
print("b. Countdown from 20 to 1:")
for i in range(20, 0, -1):
    print(i, end=' ')
print("\n")

# c. Print n stars in one line based on user input
stars = int(input("c. Number of stars: "))
print('*' * stars)

# d. Print lines of increasing stars based on user input
stars = int(input("d. Number of stars: "))
for i in range(1, stars + 1):
    print('*' * i)
