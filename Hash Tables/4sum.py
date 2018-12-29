class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        visited = {}
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                sum_remaining = target-(nums[i]+nums[j])
                if nums[i]+nums[j] in visited:
                    visited[nums[i]+nums[j]].add((i,j))
                else:
                    visited[nums[i]+nums[j]] = {(i,j)}
        result = []
        for key in visited:
            if target-key in visited:
                for (i,j) in visited[key]:
                    for (p,q) in visited[-key + target]:
                        sorted_index = sorted([nums[i], nums[j], nums[p], nums[q]])
                        if i not in (p, q) and j not in (p, q) and sorted_index not in result:
                            result.append(sorted_index)
        return result
