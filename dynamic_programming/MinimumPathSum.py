import math
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        if grid == 0 or len(grid) == 0:
            return 0
        
        no_of_rows = len(grid)
        no_of_cols = len(grid[0])
        
        dp = [[math.inf for i in range(0,no_of_cols)]for j in range(0,no_of_rows)]
        
        dp[0][0] = grid[0][0]
        
        #initializing the first row
        for i in range(1, no_of_cols):
            dp[0][i] = dp[0][i-1] + grid[0][i] 
            
        #initialize the first column
        for j in range(1, no_of_rows):
            dp[j][0] = dp[j-1][0] + grid[j][0]
            
        #filling the dp table
        for i in range(1, no_of_rows):
            for j in range(1,no_of_cols):
                if dp[i-1][j] > dp[i][j-1]:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                else:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
        
        return dp[no_of_rows-1][no_of_cols-1]
        
        
 #On leetCode, Runtime: 56 ms, faster than 85.99% of Python3 online submissions for Minimum Path Sum
