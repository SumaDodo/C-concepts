class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        if len(nums) == 1:
            return nums[0]
        
        csum = [0]*n
        csum[0] = nums[0]
        
        for i in range(1, n):
            csum[i] = csum[i-1] + nums[i]
            
        max_csum = csum[k-1]
        max_index = k-1
        
        for i in range(k, len(nums)):
            curr_sum = csum[i]-csum[i-k]
            
            if curr_sum > max_csum:
                max_csum = curr_sum
                
        return float(max_csum/k)
