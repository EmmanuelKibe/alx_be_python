#Ask the user to input the first number
num1 = int(input("Enter the first number: "))

#Ask the user to input the second number
num2 = int(input("Enter the second number: "))

#Ask the user to choose the operation
operation = input("Choose the operation (+, -, *, /): ")

# Perform the operation based on user input
match operation:
    case '+':
        result = num1 + num2
        print(f"The result of is {result}.")
    case '-':
        result = num1 - num2
        print(f"The result of is {result}.")
    case '*':
        result = num1 * num2
        print(f"The result of is {result}.")
    case '/':
        if num2 != 0:
            result = num1 / num2
            print(f"The result is {result}.")
        else:
            print("Cannot divide by zero.")
    case _:
        print("Invalid operation. Please choose from +, -, *, or /.")