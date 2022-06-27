class Solution:
    def minPartitions(self, n: str) -> int:
        """
            time complexity: O(n)
            space complexity: O(1)
        """
        return max(n)
        
        """
            time complexity: O(1)
            space complexity: O(n)
        """
        set_nums = set(n)
        for num in range(9, -1, -1):
            if str(num) in set_nums: return num
