test_case = int(input())
 
for _ in range(test_case):
    n, k_ram = map(int, input().split())
    ram_needed= list(map(int, input().split()))
    get_ram = list(map(int,input().split()))

    ram = []
    for i in range(len(ram_needed)):
        ram.append([ram_needed[i], get_ram[i]])
    ram.sort()

    i = 0
    while i < len(ram) and  ram[i][0] <= k_ram:
        k_ram += ram[i][1]
        i += 1
    
    print(k_ram)
