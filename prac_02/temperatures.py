"""
CP1404/CP5632 - Practical
Converts temperatures between Celsius and Fahrenheit.
"""

def main():
    # Get temperature in Celsius, convert it to Fahrenheit, and print the result
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is {fahrenheit}°F")

    # Get temperature in Fahrenheit, convert it to Celsius, and print the result
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F is {celsius}°C")


# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5.0 + 32


# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0 / 9.0


# Run the main function
main()
