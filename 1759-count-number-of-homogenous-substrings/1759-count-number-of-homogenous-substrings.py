class Solution:
    def countHomogenous(self, s: str) -> int:
        
        number_homogenous_substring = 0
        right = 0
        while right < len(s):
            left = right
            while right < len(s)-1 and s[right]==s[right + 1]:
                right += 1
            n = right - left + 1
            number_homogenous_substring += (n * (n +1))//2
            right += 1
        return number_homogenous_substring % ((10**9) + 7)
            