class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash Map One Pass
        # Hash Map Two Pass
        indices = {}  # num -> index
        for i, num in enumerate(nums):
            indices[num] = i
        for lower_index, num in enumerate(nums):
            difference = target - num
            higher_index = indices.get(difference, None)
            if difference in indices and higher_index != lower_index:
                return [lower_index, higher_index]
        # Sorting => O(n log n) | O(n) because we are storing the input array in a new array
        # Brute Force => O(n^2) | O(1)