class Solution:
    #first approach 
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key  = self.return_square)
        return points[:k]
    
    def return_square(self, pt: List[int]):
        return pow(pt[0], 2) + pow(pt[1],2)
      
      # def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
      # second approach
      #   d = []
      #  for i in points:
      #    value = []
      #     value.append(pow(i[0], 2) + pow(i[1], 2))
      #     value.append(i)
      #     d.append(value)
            
            
      # d.sort()
      # print(d)
      # result = []
      # a = 0
      # for i in d:
      #     if a != k:
      #         result.append(i[1])
      #     else:
      #         return result
      #     a += 1
      # return result
