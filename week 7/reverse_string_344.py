#first approach using iterative method
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        left = 0
        right = len(s)-1
        
        while left != right and left <= right:
            s[left], s[right] = s[right], s[left]
            left +=1
            right -=1
          
#second approach using recursive method
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.reverse_string(s, 0, len(s)-1)
        
    def reverse_string(self, s, left, right):
        if left > right:
            return
        else:
            s[left], s[right] = s[right], s[left]
            self.reverse_string(s, left + 1, right -1)
        
        
            
        
        
