row = 5
for i in range(1, row):
    print( " " * (row -1 -i ), "*" * ((2 * i)-1))
print()
for i in range(1, row):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
