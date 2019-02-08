#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    maximum = scores[0]
    minimum = scores[0]
    count_max = 0
    count_min = 0
    result = []
    for i in range(len(scores)):
        if scores[i]>maximum:
            maximum = scores[i]
            count_max+=1
        elif scores[i]<minimum:
            minimum = scores[i]
            count_min+=1
        else: continue
    result.append(count_max)
    result.append(count_min)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
