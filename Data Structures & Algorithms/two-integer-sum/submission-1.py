class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous_map = {}  # storing value -> index
        for i, n in enumerate(nums):
            difference = target - n
            if difference in previous_map:
                return [previous_map[difference], i]
            previous_map[n] = i

