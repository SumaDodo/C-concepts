class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #Time Complexity : O(n*k)
        #Space Complexity : O(1)
        for i in range(k):
            previous = nums[len(nums)-1]
            for j in range(len(nums)):
                temp = nums[j]
                nums[j] = previous
                previous = temp
                
