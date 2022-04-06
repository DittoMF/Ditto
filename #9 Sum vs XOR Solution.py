import math
import os
import random
import re
import sys

def sumXor(n):
    # Solution:
    
    res = 1
    n_bin = bin(n).replace('0b', '')
    
    if (n == 0):
        return 1
    
    for digit in n_bin:
        if digit == '0':
            res = res * 2
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = sumXor(n)

    fptr.write(str(result) + '\n')

    fptr.close()
