class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
    
    
        xor_val = x ^ y
        hamming_distance = 0
        
        while xor_val > 0:
            hamming_distance += 1
            xor_val = xor_val & (xor_val-1)
        return hamming_distance