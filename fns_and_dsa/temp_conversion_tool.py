FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    
temp = float(input("Input the temparature: "))
confirmation = input("Is this temparature in Celcius(C) or Farenheit(F): ")

if confirmation.strip() == 'C':
    converted_temp = convert_to_fahrenheit(temp)
    print(f"{temp}°C is {converted_temp}°F")

elif confirmation.strip() == 'F':
    converted_temp = convert_to_celsius(temp)
    print(f"{temp}°F is {converted_temp}°C") 
else:
    print("Error! Input the correct units")