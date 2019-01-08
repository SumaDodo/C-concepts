class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        c = 1
        for i in range(n):
            c = c * 2 * (2*i+1)/(i+2)
        return int(c)
