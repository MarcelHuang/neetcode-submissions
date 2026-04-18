class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash Map One Pass
        indexes = {}  # num -> index
        for i, num in enumerate(nums):
            # check first
            diff = target - num
            if diff in indexes:
                return [indexes[diff], i]  # the one in indexes is definitely lower in index than i because it was added first
            # add to map if not found
            indexes[num] = i
