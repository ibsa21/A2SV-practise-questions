class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # """time complexity: O(n)
        #    space complexity: O(n)
        # """
        # nums_dict = defaultdict(list)
        # for num in range(1, n + 1):
        #     first_char = str(num)[0]
        #     nums_dict[first_char].append(num)
        # nums = []
        # for key in nums_dict:
        #     for num in nums_dict[key]:
        #         nums.append(num)
        # return nums
    
        """
            time complexity: O(nlogn)
            space complexity: O(n)
        """
        nums = [str(num) for num in range(1, n + 1)]
        nums.sort()
        return list(map(int, nums))
