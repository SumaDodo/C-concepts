class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        element_contained = dict()
        
        for i in range(len(nums)):
            if (nums[i] in element_contained) and (i-element_contained.get(nums[i]) <= k):
                return True
            else:
                element_contained[nums[i]] = i
        
        return False
