class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = [1] * len(nums)
        prefix = 1
        suffix = 1
        for i in range(1, len(nums)):  # iterate left to right
            prefix = prefix * nums[i - 1]
            results[i] = results[i] * prefix
        for i in reversed(range(len(nums) - 1)):  # iterate right to left
            suffix = suffix * nums[i + 1]
            results[i] = results[i] * suffix
        return results
        # pass to right, pass to left
        # [1, 2, 4, 6]
        # [1*1, 1*1, 1*1*2, 1*1*2*4]  prefix
        # [1, 1, 2, 8]  prefix
        # [1*1*6*4*2, 1*1*6*4, 1*1*6, 1*1]  suffix
        # [48, 24, 6, 1]  suffix
        # [48, 24, 12, 8]
        # [2*4*6, 1*4*6, 1*2*6, 1*2*4]
