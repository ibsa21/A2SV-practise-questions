t = int(input())
for _  in range(t):
    x = int(input())
    y = list(map(int, input().split()))
    for i in set(y):
        if y.count(i) >= 2:
            y[y.index(i)] = 0 - y[y.index(i)]
    print(len(set(y)))
        
        
        

