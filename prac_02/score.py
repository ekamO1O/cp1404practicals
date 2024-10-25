""" CP1404/CP5632 - Practical
score.py """

import random


def main():
    # Ask the user for their score and print the result
    score = float(input("Enter score: "))
    result = get_score_result(score)
    print(result)

    # Generate a random score and print the result
    random_score = random.uniform(0, 100)
    print(f"Random score: {random_score}")
    print(get_score_result(random_score))


# This function determines the result based on the score
def get_score_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


# Run the main function
main()
