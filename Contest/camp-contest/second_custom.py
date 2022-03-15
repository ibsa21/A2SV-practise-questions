from audioop import reverse
import heapq
from collections import OrderedDict

n, m = map(int, input().split())
comfortable = list(map(int, input().split()))

for i in range(len(comfortable)):
    comfortable[i] = -1 * comfortable[i]

dict = OrderedDict()
difficulty = []

for i in range(n):
    number = int(input())
    difficulty.append(number)
    dict[number] = "" 

arr= difficulty[:]
difficulty.sort(reverse=True)
heapq.heapify(comfortable)

result = [0] * len(difficulty)
for i in range(len(difficulty)):

    count = 0

    while comfortable and  difficulty[i] <= -1 * comfortable[0]:
        count += 1
        heapq.heappop(comfortable)

    if result:
        result[i] = result[i-1]+ count
    else:
        result[i] = count

    if m//2 + 1 <= result[i] < m:
        dict[difficulty[i]] = "YES"
    else:
        dict[difficulty[i]] = "NO"

for key in arr:
    print(dict[key])