class Solution:
    def isPalindrome(self, s: str) -> bool:
        #amanaplanacanalpanama
        s = list(s)
        new_string = []
        for idx in range(len(s)):
            char = s[idx]
            if char.isalnum(): new_string.append(char.lower())
        
        def is_palindrome(string):
            left, right = 0, len(string)-1
            while left <= right:
                if string[left] != string[right]: return False
                left += 1
                right -= 1
            return True
        return is_palindrome(new_string)
