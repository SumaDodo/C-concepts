class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        
        depth = 1
        rows = 0
        v = [''] * numRows
        
        for i in s:
            v[rows] += i
            rows += depth
            
            if rows == numRows-1:
                depth = -1
            if rows == 0:
                depth = 1
            
        return  ''.join(v)
