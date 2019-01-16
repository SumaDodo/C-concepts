class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        path = [1]*n
        for i in range(m):
            for j in range(n):
                if i>0 and j>0:
                    path[j] += path[j-1]
                    
        return path[-1]
