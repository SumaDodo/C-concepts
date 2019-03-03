class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)== 1:
            return nums[0]
        
        sum_ = nums[0]
        result = nums[0]
        
        for i in range(1, len(nums)):
            if sum_ <= 0:
                sum_ = nums[i]
            else:
                sum_ += nums[i]
            result = max(result, sum_)
            
        return result
         
