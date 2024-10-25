"""
CP1404/CP5632 - Practical
Program that gets a score, prints a result, and shows stars using a menu.
"""


def main():
    score = get_valid_score()
    choice = ""
    while choice != "Q":
        print("\n(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")
        choice = input(">>> ").upper()

        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(determine_score_result(score))
        elif choice == "S":
            print_stars(score)
        elif choice == "Q":
            print("Farewell!")
        else:
            print("Invalid option")


# Function to get a valid score between 0 and 100
def get_valid_score():
    score = float(input("Enter a score between 0 and 100: "))
    while score < 0 or score > 100:
        print("Invalid score. Must be 0-100.")
        score = float(input("Enter a score between 0 and 100: "))
    return score


# Function to determine the result based on the score
def determine_score_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


# Function to print stars equal to the score
def print_stars(score):
    print("*" * int(score))


# Run the main function
main()
