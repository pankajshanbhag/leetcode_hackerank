#https://www.hackerrank.com/challenges/diagonal-difference

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    prim=0
    sec=0
    lenv=len(arr[0])
    for count in range(lenv):
        prim+=arr[count][count]
        sec+=arr[count][lenv-count-1]
    return abs(prim-sec)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
