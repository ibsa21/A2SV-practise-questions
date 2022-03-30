class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        if len(nums)==1:
            return 0
        
        odd_freq = {}
        even_freq = {}
        
        for i in range(len(nums)):
            if i %2==0:
                even_freq[nums[i]] = 0
            else:
                odd_freq[nums[i]] = 0
        
                
        for i in range(len(nums)):
            if i %2==0:
                even_freq[nums[i]] += 1
            else:
                odd_freq[nums[i]] +=1
        
        #find first and second largest frequent numbers in even position
        first_even, second_even = (None, 0), (None, 0)
        
        for key in even_freq:
            if even_freq[key] > first_even[1]:
                first_even, second_even = (key, even_freq[key]), first_even
            elif even_freq[key] > second_even[1]:
                second_even = (key, even_freq[key])

        #find first and second largest frequent numbers in odd position
        first_odd, second_odd = (None, 0), (None, 0)
        for key in odd_freq:
            if odd_freq[key] > first_odd[1]:
                first_odd, second_odd = (key, odd_freq[key]), first_odd
            elif odd_freq[key] > second_odd[1]:
                second_odd = (key, odd_freq[key])

        if first_odd[0] != first_even[0]:
            return len(nums) - first_odd[1] - first_even[1]
        else:
            return len(nums) - max(second_odd[1] + first_even[1], second_even[1] + first_odd[1])