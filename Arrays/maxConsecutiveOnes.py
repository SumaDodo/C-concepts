class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_count = []
        
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count = 0
            max_count.append(count)
            
        return max(max_count)
