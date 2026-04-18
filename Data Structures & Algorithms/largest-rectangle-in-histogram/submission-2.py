class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []  # start, height
        for i, current_height in enumerate(heights):
            start = i
            while stack and current_height < stack[-1][1]:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            stack.append((start, current_height))
        for start, height in stack:
            width = len(heights) - start
            area = width * height
            max_area = max(max_area, area)
        return max_area