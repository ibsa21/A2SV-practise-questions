class Solution:
    def gcdOfStrings(self,str1: str, str2: str) -> str:
        shorter = str1 if len(str1) < len(str2) else str2
        shorter_len = len(shorter)
        
        for i in range(1, shorter_len+1):
            if shorter_len % i ==0:
                sub = shorter[:shorter_len// i]
                if not str1.replace(sub,"") and not str2.replace(sub, ""):
                    return sub
        return ""
