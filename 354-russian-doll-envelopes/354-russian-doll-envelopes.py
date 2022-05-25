class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        
        def binarySearch(nums, h):
            l, r = 0, len(nums)-1

            while l <= r:
                mid = l + (r-l) // 2
                if nums[mid] == h:
                    return mid
                if nums[mid] < h:
                    l = mid + 1
                else:
                    r = mid - 1
            return l
        
        
        envelopes.sort(key= lambda x: (x[0], -x[1]))
        lis = []
        
        for w, h in envelopes:
            left = binarySearch(lis, h)
            if left == len(lis):
                lis.append(h)
            else:
                lis[left] = h
        return len(lis)