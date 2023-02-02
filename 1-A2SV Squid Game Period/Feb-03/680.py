class Solution:
    def validPalindrome(self, s: str) -> bool:

        s = list(s)
        def isPalindrome(s, left, right):
            while left <= right:
                if s[left] != s[right]:
                    return [False, (left, right)]
                left += 1
                right -= 1
            return [True]
        
        res = isPalindrome(s, 0, len(s)-1)
        if res[0] == True: return True

        left, right = res[1]
        string_a = s[:right] + s[right + 1:]
        string_b = s[:left] + s[left + 1:]

        if isPalindrome(string_a, 0, len(string_a)-1)[0] \
           or isPalindrome(string_b, 0, len(string_b)-1)[0]:
            return True

        return False