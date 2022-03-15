from ctypes.wintypes import PINT
n, m = map(int, input().split())

intervals = []
for i in range(m):
    interval = list(map(int, input().split()))
    intervals.append(interval)
intervals.sort()


mediumInterval  = intervals[0]
merged = []
for i in intervals:
    if i[0] <= mediumInterval[1]:
        mediumInterval[1] = max(i[1], mediumInterval[1])
    else:
            merged.append(mediumInterval)
            mediumInterval = i

merged.append(mediumInterval)
is_changed = False
if merged[0][0] != 0 or merged[-1][1] != n-1:
    print("YES")
    is_changed = True
else:
    for i in range(1, len(merged)):
        if abs(merged[i][0]-merged[i-1][1]) > 1:
            print("YES")
            is_changed = True
            break
if not is_changed:
    print("NO")


