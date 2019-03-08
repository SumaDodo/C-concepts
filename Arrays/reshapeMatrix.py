class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        n = len(nums)
        m = len(nums[0])
        if n*m != r*c:
            return nums
        
        new_matrix = [[0 for column in range(c)] for row in range(r)]
        row = 0
        column = 0
        
        for i in nums:
            for j in i:
                new_matrix[row][column] = j
                column += 1
                if column == c:
                    row += 1
                    column = 0
                    
        return new_matrix         
                    
