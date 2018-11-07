**Minimum Path Sum**  
This problem can be solve using recursion and Dynamic Programming.
1. Recursion:  
at every point since we can move either to right or down and never go to left, we can make a recurive call to return the minimum of path 
going to right and path going down.
'''
return min [MinPath (path going to right, path going to left)]
'''
2. Dynamic programming:  
Instead of recalculating the distance recursively, we can instead choose the best optimal from every point and only consider that 
particular path.
---
