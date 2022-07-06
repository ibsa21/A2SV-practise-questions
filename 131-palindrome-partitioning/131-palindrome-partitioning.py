class Solution:
    def partition(self, s: str) -> List[List[str]]:
        '''
            Approach: Backtrack
            Time complexity: O(len(s) * 2**len(s)-1)
            Space complexity: O(2**len(s)-1)
        '''
        def is_palindrome(string):
            l, r = 0, len(string)-1
            while l <= r:
                if string[l] != string[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        global_res = []
        local_res = []
        
        def dfs(idx):
            if idx >= len(s):
                global_res.append(local_res.copy())
                return
            
            for i in range(idx, len(s)):
                sub_string = s[idx: i + 1]
                if is_palindrome(sub_string)==True: 
                    local_res.append(sub_string)
                    dfs(i + 1)
                    local_res.pop()
        dfs(0)
        return global_res
                