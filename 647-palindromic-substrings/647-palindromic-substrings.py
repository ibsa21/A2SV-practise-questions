class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(set(s))==1:return int(len(s) * ((len(s) + 1)/2))
        
        def is_palindrome(string):
            l, r = 0, len(string)-1
            while l <= r:
                if string[l] != string[r]:return False
                l += 1
                r -= 1
            return True
        
        table = [s[-1]]
        ans = 1
        for i in range(len(s)-2, -1, -1):
            for j in range(len(table)):
                table[j] = s[i] + table[j]
            table.append(s[i])
            
            for string in table:
                if is_palindrome(string):ans += 1
        return ans