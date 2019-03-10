class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_array = sorted(nums)
        left, right = 0, len(nums)-1
        
        while(nums[left] == sorted_array[left] or nums[right] == sorted_array[right]):
            if right-left <= 1:
                return 0
            if nums[left] == sorted_array[left]:
                left += 1
            if nums[right] == sorted_array[right]:
                right -= 1
                
        return right - left + 1
