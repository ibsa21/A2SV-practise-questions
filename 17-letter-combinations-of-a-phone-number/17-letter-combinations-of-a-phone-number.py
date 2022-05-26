class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map_digit = {
                2:['a', 'b', 'c'], 3:['d', 'e', 'f'], 4:['g', 'h', 'i'], 5:['j', 'k', 'l'],
                6:['m', 'n', 'o'], 7:['p', 'q', 'r', 's'], 8:['t', 'u', 'v'], 9:['w', 'x', 'y', 'z']
                }
        res = []
        
        def dfs(idx, cur_combination):
            if len(cur_combination) == len(digits):
                if cur_combination:
                    res.append(''.join(cur_combination))
                return
            
            for char in map_digit[int(digits[idx])]:
                cur_combination.append(char)
                dfs(idx + 1, cur_combination)
                
                cur_combination.pop()
        dfs(0, [])
        return res if res else []
            