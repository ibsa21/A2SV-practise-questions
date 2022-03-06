import heapq
arr = []
N = int(input())
deleted = dict()


for i in range(N):
    instruction = input().split()
    
    if instruction[0] == '1':
        instruction = int(instruction[1])
        deleted[instruction] = 0
        heapq.heappush(arr,instruction)
    elif instruction[0] == '2':
        instruction = int(instruction[1])
        deleted[instruction] = 1
    else:
        while deleted[arr[0]] == 1:
            heapq.heappop(arr)
        print(arr[0])
