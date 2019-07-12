class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_ = 0
        for i in nums:
            sum_ ^= i
            
        return sum_
