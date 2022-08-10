class Solution:
    def validPalindrome(self, s: str) -> bool:
        s = list(s)
        
        def is_valid_palindrome(s, left, right):
            while left <= right:
                if s[left] != s[right]:
                    return [False, (left, right)]
                left += 1
                right -= 1
            return [True]
        
        res = is_valid_palindrome(s, 0, len(s)-1)
        if res[0] == True: return True
        left, right = res[1]
        string_a = s[:right] + s[right + 1:]
        string_b = s[:left] + s[left + 1:]
        print(string_a, string_b)
        if is_valid_palindrome(string_a, 0, len(string_a)-1)[0] or is_valid_palindrome(string_b, 0, len(string_b)-1)[0]:
            return True
        return False
        