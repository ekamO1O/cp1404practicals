"""CP1404 Practical, Calculating a List of Cumulative Totals"""


def main():
    """Display an income report for the specified number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    # Collect income for each month
    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    # Generate and display the income report
    print_report(incomes)


def print_report(incomes):
    """Print a detailed report of monthly incomes and cumulative totals."""
    # The length of the incomes list determines the number of months
    print("\nIncome Report\n-------------")
    total = 0
    # Enumerate provides month index starting from 1 and corresponding income
    for month, income in enumerate(incomes, 1):
        total += income
        # Print the formatted output for each month
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


main()
