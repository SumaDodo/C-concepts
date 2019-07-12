class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xor_sum = x ^ y
        bit_set = 0
        
        while (xor_sum > 0):
            bit_set += xor_sum & 1
            xor_sum >>= 1
            
        return bit_set
