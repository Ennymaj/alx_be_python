# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global conversion factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global conversion factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

if __name__ == "__main__":
    try:
        temp_input = input("Enter the temperature to convert: ").strip()
        temperature = float(temp_input)  # Will raise ValueError if invalid

        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'F':
            result = convert_to_celsius(temperature)
            print(f"{temperature}°F is {result}°C")
        elif unit == 'C':
            result = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {result}°F")
        else:
            raise ValueError("Invalid temperature unit. Please enter 'C' or 'F'.")

    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

