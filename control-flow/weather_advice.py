#Ask the user for the weather condition
weather = input("What's the weather like today? (sunny/rainy/cold): ")

# Provide advice based on the weather condition
if weather.strip().lower() == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather.strip().lower() == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather.strip().lower() == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather condition.")