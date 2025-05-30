#Ask the user to input a number they'd love to  see it's multiplication table
number = int(input("Enter a number to see its multiplication table: "))

for i in range(1, 11):
    X = number
    result = X * i
    print(f"{X} * {i} = {result}")
    print()
    i += 1