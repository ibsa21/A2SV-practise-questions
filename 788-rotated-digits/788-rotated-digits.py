class Solution(object):
    def rotatedDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        goodintegers = {0, 1, 2, 5, 6, 9, 8}
        # notvalid = {1, 11, 111, 1111, 11111, 8, 88, 888, 8888, 88888
        #             18, 118, 181, 1181, 1118, 111181, 
        #            }
        notvalid = lambda x: (len(set(x)) == 1 and (int(x[0]) in {0, 1, 8})) \
                    or (len(set(x)) == 2 and '1' in set(x) and '8' in set(x)) 
        
        ans = 0
        
        for num in range(2, n + 1):
            
            num = str(num)
            num = num.replace('0', '')
            not_found = False
            if not notvalid(num):
                for char in num:
                    if int(char) not in goodintegers:
                        not_found  = True
                        break
            
                if not not_found:
                    ans += 1
        
        return ans