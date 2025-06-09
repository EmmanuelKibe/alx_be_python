""" FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

  
temp = float(input("Input the temparature: "))
print("Invalid temperature. Please enter a numeric value.")

confirmation = input("Is this temparature in Celsius(C) or Fahrenheit(F): ")

if confirmation.strip() == 'C':
    converted_temp = convert_to_fahrenheit(temp)
    print(f"{temp}°C is {converted_temp}°F")

elif confirmation.strip() == 'F':
    converted_temp = convert_to_celsius(temp)
    print(f"{temp}°F is {converted_temp}°C") 
else:
    print("Error! Input the correct units") """

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using global conversion factor."""
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using global conversion factor."""
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# User interaction
try:
    temp_input = input("Enter the temperature to convert: ")
    temp = float(temp_input)  # Try converting to float

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == 'C':
        converted = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {converted}°F")
    elif unit == 'F':
        converted = convert_to_celsius(temp)
        print(f"{temp}°F is {converted}°C")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
