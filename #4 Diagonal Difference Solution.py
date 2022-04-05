import math
import os
import random
import re
import sys
def diagonalDifference(arr):
    # Solution:
    
    left_diagonal = 0
    right_diagonal = 0
    
    for i in range(0,len(arr)):
        left_diagonal = left_diagonal + arr[i][i]
        
    for i in range(0,len(arr)):
        right_diagonal = right_diagonal + arr[i][len(arr)-1-i]
        
    return abs(left_diagonal - right_diagonal)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
