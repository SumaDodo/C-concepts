import math

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        result = []
        for element in range(numRows):
            row = []
            for count in range(element+1):
                row.append(self.combination(element, count))
            result.append(row)
        
        return result
        
    def combination(self, n, r):
        com = int(math.factorial(n)/(math.factorial(r)*math.factorial(n-r)))
        return com
