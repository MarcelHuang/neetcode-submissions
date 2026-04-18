class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [3,4,5,6], 7
        seen = {}  # mapping of num => index
        for i, num in enumerate(nums):
            addend = target - num
            if addend in seen:
                first_index = seen[addend]
                second_index = i
                return [first_index, second_index]
            seen[num] = i

        # # BRUTE FORCE O(n^2)
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]