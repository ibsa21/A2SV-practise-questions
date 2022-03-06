#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'runningMedian' function below.
#
# The function is expected to return a DOUBLE_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def runningMedian(a):
    # Write your code here
    import heapq as h
    right = []
    left = []
    res = []
    for val in a:    
        if len(left) > len(right):
            t = h.heappushpop(left,-1*val)
            h.heappush(right,-1*t)

        else:
            t = h.heappushpop(right,val)
            h.heappush(left,-1*t)


        if len(left) > len(right):
            res.append(-1*left[0])
        else:
            res.append((-1*left[0]+right[0])/2)
        
    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    result = runningMedian(a)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
