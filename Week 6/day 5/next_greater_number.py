class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater_dict = {}

        stack = [nums2[0]]

        for i in range(1, len(nums2)):
            while(stack and nums2[i] > stack[-1]):
                greater_dict[stack.pop()] = nums2[i]
            stack.append(nums2[i])

        for j in stack:
            greater_dict[j] = -1

        return [greater_dict[i] for i in nums1]
