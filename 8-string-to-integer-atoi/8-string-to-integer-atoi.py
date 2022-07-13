class Solution:
    def myAtoi(self, s: str) -> int:
        
        # step 1: strip leading space
        s = s.lstrip()
        # step 2: determine the sign
        sign = '+'
        if s and  (s[0]=='+' or s[0]=='-'):
            if s[0] == '-':
                sign  = '-'
            s = s[1:]
        
        #step 3: strip characters after non-digits
        for idx, char in enumerate(s):
            if char.isdigit() == False:
                s = s[:idx]
                break
        if not s: return 0
        num = -int(s) if sign == '-' else int(s)
        
        left_boundary = pow(-2, 31)
        right_boundary =  pow(2, 31) - 1
        if num < left_boundary: num = left_boundary
        if num > right_boundary: num = right_boundary
        return num