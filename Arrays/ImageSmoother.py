from math import floor

class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        m = len(M)
        n = len(M[0])
        smoothing_val = []
        dx, dy = [-1,0,1], [-1, 0, 1]
        
        
        for i in range(m):
            row_val = []
            for j in range(n):
                val = [M[i+x][j+y] for x in dx for y in dy \
                if 0 <= i+x < m and 0 <= j+y < n]
                row_val.append(floor(sum(val)/len(val)))
            smoothing_val.append(row_val)

        return smoothing_val
