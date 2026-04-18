class Solution:
    def trap(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        while left < right:
            if left_max <= right_max:
                left += 1
                block_of_water = left_max - height[left]
                if block_of_water > 0:
                    max_area += block_of_water
                left_max = max(left_max, height[left])
            else:
                right -= 1
                block_of_water = right_max - height[right]
                if block_of_water > 0:
                    max_area += block_of_water
                right_max = max(right_max, height[right])
        return max_area