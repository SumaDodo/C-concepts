class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        if len(nums) == 0:
            return 0
        for i in range(len(nums)):
            if nums[i] != val:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                j+=1
        return j
