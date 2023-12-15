# Function to convert length units
def convert_length(value, source_unit, target_unit):
    conversion_factors = {
        'meters': 1.0,
        'feet': 3.28084,
        'inches': 39.3701,
        'centimeters': 100,
    }

    try:
        value = float(value)
    except ValueError:
        return "Error: Please enter a valid numeric value."

    if source_unit not in conversion_factors or target_unit not in conversion_factors:
        return "Error: Unsupported units. Supported units are meters, feet, inches, and centimeters."

    result = value * conversion_factors[source_unit] / conversion_factors[target_unit]
    return f"{value} {source_unit} is equal to {result:.2f} {target_unit}."

# Function to get user input
def get_user_input():
    value = input("Enter the value to convert: ")
    source_unit = input("Enter the source unit (e.g., meters, feet, inches, centimeters): ").lower()
    target_unit = input("Enter the target unit (e.g., meters, feet, inches, centimeters): ").lower()

    return value, source_unit, target_unit

# Main program
if __name__ == "__main__":
    print("Welcome to the Unit Converter!")

    while True:
        try:
            value, source_unit, target_unit = get_user_input()
            result = convert_length(value, source_unit, target_unit)
            print(result)
        except Exception as e:
            print(f"An error occurred: {str(e)}")

        try_again = input("Do you want to perform another conversion? (yes/no): ").lower()
        if try_again != 'yes':
            break

    print("Thank you for using the Unit Converter!")
