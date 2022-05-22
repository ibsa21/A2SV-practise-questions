class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right_product, left_product= [nums[0]], deque()
        for i in range(1, len(nums)):
            right_product.append(right_product[i-1] * nums[i])
            
        left_product.append(nums[-1])
        for i in range(len(nums)-2, -1, -1):
            left_product.appendleft(left_product[0] * nums[i])
        ans = [left_product[1]]
        for i in range(1, len(nums)-1):
            ans.append(left_product[i+1] * right_product[i - 1])
        ans.append(right_product[-2])
        return ans