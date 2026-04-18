class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Idea: move the pointer with smaller height
        # because that's the one that's going to increase the volume of water
        left = 0
        right = len(heights) - 1
        result = 0
        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            area = width * height
            result = max(result, area)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return result