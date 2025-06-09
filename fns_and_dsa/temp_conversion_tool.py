FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
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
    print("Error! Input the correct units")