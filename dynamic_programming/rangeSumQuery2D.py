class NumMatrix:

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        if matrix is None or not matrix:
            return 
        no_of_rows = len(matrix)
        no_of_cols = len(matrix[0])
        self.values = [[0 for i in range(no_of_cols+1)] for j in range(no_of_rows+1)]
        
        for i in range(1,no_of_rows+1):
            for j in range(1, no_of_cols+1):
                self.values[i][j] = self.matrix[i-1][j-1]+self.values[i][j-1]+self.values[i-1][j]-self.values[i-1][j-1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1
        return self.values[row2][col2] - self.values[row2][col1-1] - self.values[row1-1][col2] + self.values[row1-1][col1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
