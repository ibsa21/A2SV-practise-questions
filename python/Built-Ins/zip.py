# Enter your code here. Read input from STDIN. Print output to STDOUT
N, X = map(int, input().split())
marks = []
for i in range(X):
    marks.append(list(map(float, input().split())))
zippedList = list(zip(*marks))
total = 0
for i in range(len(zippedList)):
    total = sum(zippedList[i])
    print(total/X)
