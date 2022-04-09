class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        
        def find_left(index):
            
            if index==0:
                return True
            
            return flowerbed[index-1] == 0
        
        def find_right(index):
            
            if index == len(flowerbed)-1:
                return True
            
            
            return flowerbed[index+1] == 0

                
            
        for i in range(len(flowerbed)):
            
            if flowerbed[i] == 0:
                
                if find_left(i) and find_right(i):
                    flowerbed[i] =1
                    n-=1
        return n <= 0