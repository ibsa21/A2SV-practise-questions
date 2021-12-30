N = int(input())
for _ in range(2):
    for i in range(1, N+1):
        if N == 1:
            print("#", end = " ")
        else:
            print("#" * (N -1), end = " ")
    print()
