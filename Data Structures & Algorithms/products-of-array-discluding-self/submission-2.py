class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # pass to right, pass to left
        # [1, 2, 4, 6]
        # [1*1, 1*1, 1*1*2, 1*1*2*4]  prefix
        # [1, 1, 2, 8]  prefix
        # [1*1*6*4*2, 1*1*6*4, 1*1*6, 1*1]  suffix
        # [48, 24, 6, 1]  suffix
        # [48, 24, 12, 8]
        # [2*4*6, 1*4*6, 1*2*6, 1*2*4]

        left_product   = [1] * len(nums)
        right_product  = [1] * len(nums)
        results        = [1] * len(nums)
        prefix = 1
        suffix = 1
        for i in range(1, len(nums)):
            prefix *= nums[i - 1]
            left_product[i] *= prefix
        print(left_product)
        for i in reversed(range(len(nums) - 1)):
            suffix *= nums[i + 1]
            right_product[i] *= suffix
        print(right_product)
        for i in range(len(results)):
            results[i] = left_product[i] * right_product[i]
        return results

















































        
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
