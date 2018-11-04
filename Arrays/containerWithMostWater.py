class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right, area = 0, len(height)-1, 0
        while (left < right):
            if height[left] >= height[right]:
                area = max(area,(right-left)*height[right])
                right = right -1
            else:
                area = max(area, (right-left)*height[left])
                left = left + 1
        return area
