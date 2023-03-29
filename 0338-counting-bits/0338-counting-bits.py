class Solution:
    def countBits(self, n: int) -> List[int]:
        
        answer = [0]
        
        for val in range(1, n+1):
            if val %2 == 0:
                answer.append(answer[val//2])
            else:
                answer.append(answer[val//2]+1)
        return answer