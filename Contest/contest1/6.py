nums = list(map(int, input().split()))
num = sorted(nums)
for _ in range(num.count(0)):
    nums.remove(0)
zero = [0] * num.count(0)
nums  = nums + zero
print(nums)