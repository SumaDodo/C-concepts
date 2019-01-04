class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return -1 * self.helperFunction(-x)
        return self.helperFunction(x)
    
    def helperFunction(self, x):
        result = 0
        while x != 0:
            num = x % 10
            result = result * 10 + num
            x = int(x/10)
        
        return 0 if result > pow(2, 31) - 1 or result < -pow(2, 31) else result
