""" Exceptions To Complete """

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # TODO: this line sets the loop to stop once a valid integer is entered
    except ValueError:  # TODO - specify ValueError to catch non-integer inputs
        print("Please enter a valid integer.")
print("Valid result is:", result)
