class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 0. Initialize results, prefix, and postfix
        #    1,     , [1,2,4,6],       1
        # prefix                    postifx
        # 1. Loop through nums: res *= prefix , prefix  *= nums
        # 2. Loop through nums: res *= postfix, postfix *= nums
        results = [1] * len(nums)
        prefix  = 1
        postfix = 1
        for i in range(len(nums)):
            results[i] *= prefix
            prefix     *= nums[i]
        for i in reversed(range(len(nums))):
            results[i] *= postfix
            postfix    *= nums[i]
        return results
