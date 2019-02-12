from sys import stdin, stdout
import numpy as np

# array = []
no_test_cases = stdin.readline()
n,sum_ = stdin.readline().split()
array= (stdin.readline().split())

array_ = [int(i) for i in array]

# print(array_)
result = 0
for i in range(int(n)):
    result = array_[i]
    j = i+1
    while j<=int(n):
        if result == int(sum_):
            print(i+1, j)
        if result > int(sum_) or j==int(n):
            break
        result = result + array_[j]
        j+=1
