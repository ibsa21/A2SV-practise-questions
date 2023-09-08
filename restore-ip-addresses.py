class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        answer = []
        def isValid(address, length):
            if len(address) < length or int(address[:length]) > 255:
                return False
            if length > 1 and address[0] == '0':
                return False
            return True

        def backtrack(remaining, path):
            
            if len(path) > 4:
                return 

            if not remaining:
                if len(path) == 4:
                    answer.append('.'.join(path))
                return 
                
            single = remaining[0]
            backtrack(remaining[1:], path + [single])
            if isValid(remaining, 2):
                backtrack(remaining[2:], path + [remaining[:2]])
            if isValid(remaining, 3):
                backtrack(remaining[3:], path + [remaining[:3]])
            
            return 
        backtrack(s, [])
        return answer