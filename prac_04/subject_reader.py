"""CP1404 Practical, Converting Data Strings to Lists"""

FILENAME = "subject_data.txt"


def main():
    """Read subject data and display it neatly."""
    subjects = load_subjects()  # Load subjects from the file
    display_subjects(subjects)   # Display the subject data


def load_subjects():
    """Load data from file formatted as: code, lecturer, number_of_students."""
    subjects = []  # List to hold subject information
    input_file = open(FILENAME)  # Open the file
    for line in input_file:
        line = line.strip()  # Remove whitespace and newline
        parts = line.split(',')  # Split the line into parts
        parts[2] = int(parts[2])  # Convert student count to integer
        subjects.append(parts)  # Add to the subjects list
    input_file.close()  # Close the file
    return subjects  # Return the list of subjects


def display_subjects(subjects):
    """Display subject data in a formatted way."""
    for subject in subjects:
        print("{} is taught by {:12} and has {:3} students".format(*subject))


main()
# Run the main function
