# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
from collections import defaultdict

d = defaultdict(list)
n, m = (int(i) for i in input().split())

for i in range(n):
    d[input()].append(i+1)

for j in range(m):
    print(*d.get(input(),[-1]), sep=" ")
