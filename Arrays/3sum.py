class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        
        result = []
        
        for i in range(len(nums)-2):
            current_number = nums[i]
            left = i+1
            right = len(nums)-1
            while (left<right):
                total_sum = nums[left]+nums[right]
                if total_sum == -current_number:
                    result.append([nums[left], nums[right], current_number])
                    right -= 1
                    left += 1
                elif total_sum > -current_number:
                    right -= 1
                else:
                    left += 1
        
        unique_data = [list(x) for x in set(tuple(x) for x in result)]
        return unique_data
