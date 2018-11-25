from numpy import shape
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        no_of_rows = len(obstacleGrid)
        no_of_cols = len(obstacleGrid[0])
        
        unique_paths = [[0] * no_of_rows]* no_of_cols

        for p in range(no_of_rows):
            if obstacleGrid[p][0] != 1:
                unique_paths[p][0] = 1
            else:
                break

        for j in range(no_of_cols):
            if obstacleGrid[0][j] != 1:
                unique_paths[0][j] = 1
            else:
                break

        for k in range(1,no_of_rows):
            for x in range(1,no_of_cols):
                if obstacleGrid[k][x] != 1:
                    unique_paths[k][x] = unique_paths[k - 1][x] + unique_paths[k][x - 1]
                else:
                    unique_paths[k][x] = 0

        return unique_paths[no_of_rows - 1][no_of_cols - 1]
