class Solution:
    def maxSubarrayLength(self, nums: List[int]) -> int:
        
        smallestRight = nums[::]
        
        for index in range(len(nums)-2, -1, -1):
            smallestRight[index] = min(smallestRight[index], smallestRight[index+1])
        
        # print(smallestRight)
        left = 0
        answer = 0
        # print('hello')
        for index in range(len(nums)):
            rightSide = nums[index]
            right_index = bisect_left(smallestRight, rightSide)
            # print(nums[index], right_index, index)
            answer = max(answer, right_index - index)
        
        return answer