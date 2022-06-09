import copy
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        level = int(math.floor(math.log(label, 2))) + 1
        
        
        tree = []
        
        num = 1
        for i in range(level):
            nums = deque()
            for _ in range(pow(2, i)):
                if i % 2 != 0:
                    nums.appendleft(num)
                else:
                    nums.append(num)
                num += 1
            tree.extend(nums)
        
        parent = lambda i : int(math.ceil(i/2)) - 1
        left = lambda i : 2 * i + 1
        right = lambda i : 2 * i  + 2
        
        ans = deque()
        i = tree.index(label)
        while i >= 0:
            ans.appendleft(tree[i])
            i = parent(i)
        
        return list(ans)