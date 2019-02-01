#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    first_diagonal_sum = 0
    second_diagonal_sum = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if i==j:
                first_diagonal_sum += arr[i][j]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if i == n-1-j:
                second_diagonal_sum+=arr[i][j]

    diff = abs(first_diagonal_sum-second_diagonal_sum)
    return diff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
