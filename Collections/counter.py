# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
from collections import Counter

no_of_shoes = int(input())
shoes = Counter(map(int, input().split()))

no_of_customers = int(input())
total_money = 0
for i in range(no_of_customers):
    (size, price) = map(int,input().split())

    if shoes[size]>0:
        total_money+=price
        shoes[size]-=1

print (total_money)
