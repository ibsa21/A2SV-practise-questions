class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        length = len(s1)
        s1_counter = Counter(s1)
        for right, char in enumerate(s2):
            counter = Counter(s2[right:min(len(s2), right + len(s1))])
            isFound = True
            for key, value in s1_counter.items():
                if key not in counter or counter[key] != value:
                    isFound = False
                    break
            if isFound:
                return True
        return False