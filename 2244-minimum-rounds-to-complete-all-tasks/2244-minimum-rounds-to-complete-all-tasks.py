class Solution(object):
    def minimumRounds(self, tasks):
        """
        :type tasks: List[int]
        :rtype: int
        """
        counter = Counter(tasks)
        print(counter)
        
        ans = 0
        for key in counter:
            if counter[key] < 2:return -1
            ans += math.ceil(counter[key]/3.0)
        
        return int(ans)
            
            