# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
listN = input().split()
print(all([int(x) > 0 for x in listN]) and  any([listN[i] == listN[i][::-1] for i in range(N)]))
