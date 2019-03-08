class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        i = 0
        j = 0
        output = 0
        
        while j < n:
            j = i+1
            output += min(nums[i], nums[j])
            i += 2
            j += 1
            
        return output
