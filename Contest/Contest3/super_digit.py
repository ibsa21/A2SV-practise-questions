#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    super_digit  = ""
    total_sum = 0
    for num in n:
        total_sum += int(num)
    total_sum *=k
    super_digit = str(total_sum)
    
    print(super_digit)
    while len(super_digit) > 1:
        total_sum = 0
        
        for i in range(len(super_digit)):
            total_sum += int(super_digit[i])
        super_digit = str(total_sum)
        print(super_digit)
    
    return super_digit
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
