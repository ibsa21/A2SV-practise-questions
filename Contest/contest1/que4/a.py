rows = 3
for i in range(1, rows + 1):
    print(" " * (rows - i), end=" ")
    for j in range(1, i + 1):
        print(j, end="")
    for k in list(reversed(range(1, i))):
        print(k, end="")
    print()

# second for loop to print the lower section of the diamond
for i in range(rows -1, 0, -1):
    print(" " * (rows - i), end=" ")
    for j in range(1, i + 1):
        print(j, end="")
    for k in list(reversed(range(1, i))):
        print(k, end="")
    print()
