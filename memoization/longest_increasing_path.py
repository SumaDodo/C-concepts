class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        if row == 0:
            return 0

        col = len(matrix[0])


        def dfs(x, y):
            for dx, dy in zip([1, 0, -1, 0], [0, 1, 0, -1]):
                nx, ny = x + dx, y + dy
                if 0 <= nx < row and 0 <= ny < col and matrix[nx][ny] > matrix[x][y]:
                    if not dp[nx][ny]: dp[nx][ny] = dfs(nx, ny)
                    dp[x][y] = max(dp[x][y], 1 + dp[nx][ny])
            dp[x][y] = max(dp[x][y], 1)
            return dp[x][y]


        dp = [[0] * col for i in range(row)]
        for i in range(row):
            for j in range(col):
                if not dp[i][j]:
                    dp[i][j] = dfs(i, j)
        return max([max(x) for x in dp])
