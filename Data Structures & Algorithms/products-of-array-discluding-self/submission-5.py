class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # two pass prefix postfix
        res = [1 for i in range(len(nums))]
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in reversed(range(len(nums))):
            res[i] *= postfix
            postfix *= nums[i]
        return res