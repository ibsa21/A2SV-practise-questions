class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        
        ans = 0
        freqMap = defaultdict(int)
        print(sum(deliciousness))
        for num in deliciousness:
            for i in range(22):
                ans += freqMap[2**i-num]
            freqMap[num] += 1
        return ans % ((10**9) + 7)