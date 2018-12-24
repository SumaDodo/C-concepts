class Solution:  
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mapping = dict()
        for index,numbers in enumerate(nums):
            remaining = target - numbers
            if remaining in mapping:
                return [mapping[remaining],index]
            else:
                mapping[numbers] = index
        
