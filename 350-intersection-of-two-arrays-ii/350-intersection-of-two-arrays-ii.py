class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count_nums1 = Counter(nums1)
        count_nums2 = Counter(nums2)
        
        res = []
        for key, value in count_nums1.items():
            if key in count_nums2:
                res.extend([key] * min(value, count_nums2[key]))
        return res