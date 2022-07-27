class Solution:
    def countSubarrays(self, a: List[int], k: int) -> int:
        n = len(a)
        left, cur_sum, ans = 0, 0, 0

        for right in range(n):
            cur_sum += a[right]
            while cur_sum * (right - left + 1) >= k:
                cur_sum -= a[left]
                left += 1
            ans += right - left + 1
        return ans