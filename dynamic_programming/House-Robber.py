class Solution:
  def rob(self,nums):
    length = len(nums)
    map = {}
    def helper_func(i):
      if length-1 == i:
        return nums[i]
       if i>= length: return 0
       if i in map: return map[i]
       sum1 = nums[i] + helper_func(i+2)
       sum2 = nums[i+1] + helper_func(i+3)
       map[i] = max(sum1,sum2)
       return map[i]
   return helper_func(0)
   
