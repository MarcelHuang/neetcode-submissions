class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Idea: Find the area by moving the smaller height pointer
        max_area = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            width  = right - left
            height = min(heights[left], heights[right])
            area = width * height
            max_area = max(max_area, area)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return max_area
