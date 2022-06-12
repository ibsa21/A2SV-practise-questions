class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def getString(s):
            texta  = []        
            for idx, char in enumerate(s):
                if char == '#' and texta:
                    texta.pop()
                elif char != '#':
                    texta.append(char)

            return ''.join(texta)
        
        return getString(s)==getString(t)
        