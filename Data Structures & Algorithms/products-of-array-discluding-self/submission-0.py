class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        [1,2,4,6]
        [1,2,8,48]
        [8,8,4,1]
        [1,1,1,1]
        prefix  = 1
        results = [1] * len(nums)
        for i in range(len(nums)):
            results[i] *= prefix
            prefix     *= nums[i]
        postfix = 1
        for i in reversed(range(len(nums))):
            results[i] *= postfix
            postfix    *= nums[i]
        return results
