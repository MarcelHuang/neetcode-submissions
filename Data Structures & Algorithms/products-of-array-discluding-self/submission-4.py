class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # two pass, left and right, carry over
        [1 , 2 , 4, 6]
        [1 , 1 , 2, 8]
        [48, 24, 6, 1]
        left_products = [1 for i in range(len(nums))]
        right_products = [1 for i in range(len(nums))]
        carry = 1
        for i in range(1, len(nums)):
            carry *= nums[i - 1]
            left_products[i] = carry
        carry = 1
        for i in reversed(range(len(nums) - 1)):
            carry *= nums[i + 1]
            right_products[i] = carry
        print(left_products)
        print(right_products)
        return [left_products[i] * right_products[i] for i in range(len(nums))]
        