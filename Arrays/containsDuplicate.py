from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        element_count = Counter(nums)
        
        for key,values in element_count.items():
            if values > 1:
                return True
            
        return False
