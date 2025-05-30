#Ask the user to input the size of a pattern
size = int(input("Enter the size of the pattern: "))
i = 1

while i <= size:
    for row in range(1, size + 1):
        print("*", end=" ")
    print()
    i += 1