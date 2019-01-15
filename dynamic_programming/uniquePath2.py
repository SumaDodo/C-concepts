class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        path = [1]*cols
        
        for i in range(rows):
            for j in range(cols):
                if obstacleGrid[i][j]==1:
                    path[j] = 0
                    continue
                if i==0 and j>0:
                    path[j] = path[j-1]
                if i>0 and j>0:
                    path[j] += path[j-1]
                    
        return path[-1]
