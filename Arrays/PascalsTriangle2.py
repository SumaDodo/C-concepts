import math

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = []
        for element in range(rowIndex+1):
            row = []
            for count in range(element+1):
                row.append(self.combination(element, count))
            result.append(row)
        
        final_ = result[rowIndex]
        return final_
        
    def combination(self, n, r):
        com = int(math.factorial(n)/(math.factorial(r)*math.factorial(n-r)))
        return com
