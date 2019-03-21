class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        n = len(nums)
        max_element = max(nums)
        index = 0
        
        for i in range(n):
            if nums[i] != max_element:
                if max_element < 2*nums[i]:
                    return -1
        
        return nums.index(max_element)
