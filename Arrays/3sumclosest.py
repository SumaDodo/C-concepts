class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = []
        if len(nums)>0:
            for i in range(len(nums)-2):
                number = nums[i]
                left = i+1
                right = len(nums)-1
                while(left<right):
                    total_sum = nums[left]+nums[right]+number
                    if total_sum == target:
                        return total_sum
                    elif total_sum > target:
                        right = right -1
                    else:
                        left = left + 1
                    result.append(total_sum)
            return min(result, key = lambda x:abs(x-target) )
                    
            
        
