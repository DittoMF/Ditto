import math
import os
import random
import re
import sys

def compareTriplets(a, b):
    #solution
    rating_a = 0
    rating_b = 0
    for i in range(0,3):
        if a[i] > b[i]:
            rating_a += 1
        elif b[i] > a[i]:
            rating_b += 1
        else:
            pass
    return [rating_a,rating_b]
     
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
