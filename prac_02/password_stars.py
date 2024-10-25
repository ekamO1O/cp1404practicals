""" CP1404/CP5632 - Practical
Password Check with Functions """

MIN_LENGTH = 8  # Set the minimum length for the password


def main():
    password = get_password()
    print_asterisks(password)


# This function gets a valid password from the user
def get_password():
    password = input("Enter your password: ")
    while len(password) < MIN_LENGTH:
        print("Password must be at least", MIN_LENGTH, "characters long.")
        password = input("Enter your password: ")
    return password


# This function prints asterisks based on the password length
def print_asterisks(password):
    print('*' * len(password))


main()  # Call the main function to run the program

