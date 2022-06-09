class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        taken = []
        for i in range(len(seats)):
            if seats[i] == 1:
                taken.append(i)
        
        ans = 0
        for i in range(1, len(taken)):
            ans = max(ans, math.ceil((taken[i] - taken[i-1])/2))
        
        if taken[0] != 0:
            ans = max(ans, taken[0])
        
        if taken[-1] != len(seats) -1 :
            ans = max(ans, len(seats)-1 - taken[-1])
        return int(ans)