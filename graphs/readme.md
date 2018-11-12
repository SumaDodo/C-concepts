
**BellmanFord Algorithm**
- The relax operation is to check if there exists a distance to node n such that the current distance is larger, then update the distance to the new distance
- set the parent to the source from which the edge arises


if the graph is a sparse graph then run time complexity of bellmanford algorithm is O(n^2)  
if the graph is really dense then the run time complexity is even more high i.e. O(n^3)

---
**Minimum Height Trees**  
- Path graph is a tree with two nodes of vertex degree 1 and the rest n-2 nodes with the vertex degree 2. Thus, it is a graph that can be drawn such that the edges and vertices lie on the same straight line <sup>1</sup>

**References**  
1. [Path Graph](http://mathworld.wolfram.com/PathGraph.html)
