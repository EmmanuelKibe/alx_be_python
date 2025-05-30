#Ask the user to input a number they'd love to  see it's multiplication table
number = int(input("Enter a number to see its multiplication table: "))

for i in range(1, 11):
    Y = i
    Z = number * Y
    print(f"{number} * {Y} = {Z}")
    print()
    i += 1