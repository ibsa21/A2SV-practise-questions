class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        l, r, total_combination = 0, k-1, pow(2, k)
        binary_comb  = set()
        while r < len(s):
            bin_string = s[l:r+1]
            if bin_string not  in binary_comb:
                binary_comb.add(bin_string)
                if len(binary_comb) == total_combination: return True
            r += 1
            l += 1
        return False