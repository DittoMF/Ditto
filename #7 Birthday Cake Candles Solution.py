import math
import os
import random
import re
import sys

def birthdayCakeCandles(candles):
#Solution:
    candles.sort()
    
    output = candles.count(candles[len(candles)-1])
    return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
