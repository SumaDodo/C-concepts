from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element_count = Counter(nums)
        max_ = 0
        max_key = 0
        
        for key,value in element_count.items():
            if value > max_ :
                max_ = value
                max_key = key
                
        return max_key
