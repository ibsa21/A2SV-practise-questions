rows = 4
for i in range(1, rows + 1):
    print("*" * i, end="")
    print(" " * ((rows - i) * 2), end="")
    print("*" * i)
