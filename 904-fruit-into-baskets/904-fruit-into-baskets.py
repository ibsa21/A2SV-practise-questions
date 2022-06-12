class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
#         [1,0,1,4,1,4,1,2,3]
        l,r = 0, 0
        my_dict = defaultdict(int)
        ans = 0
        
        while r < len(fruits):
            my_dict[fruits[r]] +=1 
            while len(my_dict.keys()) > 2:
                my_dict[fruits[l]] -= 1
                if my_dict[fruits[l]] < 1:
                    del my_dict[fruits[l]]
                l += 1
            ans = max(ans, r - l + 1)
            r += 1
        
        return ans
                