class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left = 0
        right = len(s) -1
        new_string = []
        while left <= right:
            if s[left].isalnum():
                new_string.append(s[left].lower())
            left += 1
        
        left, right = 0, len(new_string) -1
        while left <= right:
            if new_string[left] != new_string[right]:return False
            left += 1
            right -= 1
                
        return True
            