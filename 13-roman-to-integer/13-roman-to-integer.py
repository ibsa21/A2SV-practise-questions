class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman_toint = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        
        res = 0
        
        i  = 0
        while i < len(s):
            one_roman = s[i]
            two_roman = s[i:i + 2]
            
            if two_roman in roman_toint:
                res += roman_toint[two_roman]
                i += 2
            else:
                res += roman_toint[one_roman]
                i += 1
        return res