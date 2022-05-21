class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = Counter(magazine)
        for str_k in ransomNote:
            if str_k not in count or count[str_k] <=0:
                return False
            count[str_k] -=1
        return True