class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return list(map(str, bin(n)[3:])).count('1')==0 and n!=0