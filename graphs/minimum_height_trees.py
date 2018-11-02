class Solution:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        #stopping condition
        if n == 1: return [0]
        adjacent_nodes = [set() for _ in range(n)]
        for i,j in edges:
            adjacent_nodes[i].add(j)
            adjacent_nodes[j].add(i)
            
        #What are leaves?
        leaves = [i for i in range(n) if len(adjacent_nodes[i])==1]
        
        while n>2:
            n = n - len(leaves)
            newLeaves = []
            for i in leaves:
                j = adjacent_nodes[i].pop()
                adjacent_nodes[j].remove(i)
                if len(adjacent_nodes[j]) == 1:
                    newLeaves.append(j)
            leaves = newLeaves
        return leaves
