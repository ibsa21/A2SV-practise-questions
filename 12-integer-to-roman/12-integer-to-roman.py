class Solution:
    def intToRoman(self, num: int) -> str:
        hash_table = {1:'I', 5:'V', 10:'X', 50:'L' , 100:'C', 500:'D', 1000:'M',
                      4:'IV', 9:'IX', 40:'XL', 90:'XC', 400:'CD', 900:'CM'}
        roman_order = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        i, result = 0, []
        
        while num > 0:
            if num  - roman_order[i] >=0:
                num -= roman_order[i]
                result.append(hash_table[roman_order[i]])
            else:i +=1
                
        return ''.join(map(str, result))
