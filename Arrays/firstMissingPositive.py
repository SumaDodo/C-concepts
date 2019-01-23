class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i, v in enumerate(nums):
            if v < 1:
                nums[i] = len(nums) + 1
                
        for i in range(len(nums)):
            index = abs(nums[i])-1
            if index < len(nums) and 0 < nums[index]:
                nums[index] = -nums[index]
                
        for i in range(len(nums)):
            if nums[i]>-1:
                return i+1
        return len(nums)+1
