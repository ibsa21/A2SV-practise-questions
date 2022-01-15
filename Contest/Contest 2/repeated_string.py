#!/bin/python3

import math
import os
import random
import re
import sys
import collections

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    occurence =collections.Counter(s)
    
    remainder = n  % len(s)
    number = n// (len(s))
    for key, value in occurence.items():
            occurence[key] *= number
    if remainder !=0:
        string  = s[:n % len(s)]
        key_value = collections.Counter(string)
        print(key_value['a'])
        for key, value in key_value.items():
            occurence[key] += value
        
    return occurence['a']
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
