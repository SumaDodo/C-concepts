#Method 1: Time Limit Exceeded
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
                
#Method 2: Run tie 76ms. Time Complexity: O(n) space: O(n)
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        new = [None]*len(nums)
        for i in range(len(nums)):
            new[(i+k)%len(nums)] = nums[i]
            
        for i in range(len(nums)):
            nums[i] = new[i]
                
