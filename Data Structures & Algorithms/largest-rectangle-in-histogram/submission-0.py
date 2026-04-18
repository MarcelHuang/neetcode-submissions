class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Time Complexity: O(n) - each element is pushed and popped at most once
        # Space Complexity: O(n) - stack can store at most n elements
        
        maxArea = 0
        stack = []  # stores tuples of (index, height)
        
        # Process each bar in the histogram
        for i, h in enumerate(heights):
            start = i  # potential start index for the current height
            
            # While stack has bars higher than current bar,
            # we need to pop and calculate their areas
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                # Calculate area with the popped bar as the limiting height
                # Width = current index - start index of the popped bar
                area = height * (i - index)
                maxArea = max(maxArea, area)
                start = index  # Update start to the leftmost possible position
            
            # Push current bar with its leftmost possible position
            stack.append((start, h))
        
        # Process remaining bars in stack
        # These bars extend to the right edge of histogram
        for i, h in stack:
            # Width = total length - start index of current bar
            area = h * (len(heights) - i)
            maxArea = max(maxArea, area)
            
        return maxArea