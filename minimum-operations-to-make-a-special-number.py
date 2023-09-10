class Solution:
   def minimumOperations(self, num: str) -> int:

       five_found = False
       zero_found = False
       for i in range(len(num)-1, -1, -1):

           if zero_found and (num[i] in {'0', '5'}):
               return len(num) - 2 - i
           if five_found and (num[i] in {'2', '7'}):
               return len(num) - 2 - i
               
           if num[i] == '5':
               five_found = True
           if num[i] == '0':
               zero_found = True

       return len(num) if not zero_found else len(num)-1