# https://www.hackerrank.com/challenges/compare-the-triplets/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    C = sum([1 if x[0] > x[1] else 0 for x in zip(a,b)])
    D = sum([1 if x[1] > x[0] else 0 for x in zip(a,b)])

    return (C, D)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
