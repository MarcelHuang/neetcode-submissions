class Solution:
    def trap(self, height: List[int]) -> int:
        # Idea: Find the area of water at each height by
        # min(leftmax, rightmax) - current_height with 2 pointers
        max_area = 0
        left = 0
        right = len(height) - 1
        left_max = [0] * len(height)
        current_left_max = 0
        for i in range(1, len(height)):
            current_left_max = max(current_left_max, height[i - 1])
            left_max[i] = current_left_max
        print(left_max)
        right_max = [0] * len(height)
        current_right_max = 0
        for i in reversed(range(len(height) - 1)):
            current_right_max = max(current_right_max, height[i + 1])
            right_max[i] = current_right_max
        print(right_max)
        for i, h in enumerate(height):
            length = min(left_max[i], right_max[i])
            area_of_water = length - h
            if area_of_water > 0:
                max_area += area_of_water
        return max_area