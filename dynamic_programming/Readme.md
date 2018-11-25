**Minimum Path Sum**  
This problem can be solve using recursion and Dynamic Programming.
1. Recursion:  
at every point since we can move either to right or down and never go to left, we can make a recurive call to return the minimum of path 
going to right and path going down.
```
return min [MinPath (path going to right, path going to left)]
```
2. Dynamic programming:  
Instead of recalculating the distance recursively, we can instead choose the best optimal from every point and only consider that 
particular path.

---
**Edit Distance**  
1. It is the algorithm to measure how dissimilar two strings are by measuring the minimum number of operations required to convert one string to another.
2. Used in automatic spelling correction.
3. Levenshtein distance is equal to minimum number of operations required to transform a to b.
