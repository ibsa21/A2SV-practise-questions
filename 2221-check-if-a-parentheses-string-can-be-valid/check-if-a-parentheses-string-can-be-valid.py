class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        
        if len(s) %2 != 0:
            return False
        
        balance = 0
        
        for index, sign in enumerate(s):
            if sign == '(' or locked[index] == '0':
                balance += 1
            else:
                balance -= 1
                
            if balance < 0:
                return False
        
        balance = 0
        for index in range(len(s)-1, -1, -1):
            if s[index] == ')' or locked[index] == '0':
                balance += 1
            else:
                balance -= 1
            
            if balance < 0:
                return False
        
        return True
                