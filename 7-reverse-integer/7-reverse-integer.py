class Solution:
    def reverse(self, x: int) -> int:
        if x >  0:x = str(x)
        else:
            x = str(x * -1)
            x += '-'
        res = int(x[::-1])
        return 0 if  res < -1 * pow(2, 31) or res > pow(2, 31)  else res
