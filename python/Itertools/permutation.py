# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
S, k  = input().split()
S = list(S)
S.sort()
for i in permutations(S, int(k)):
    print("".join(i))
