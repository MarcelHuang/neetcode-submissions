class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Brute Force
        # for i in range(len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
        unique = set()
        for num in nums:
            if num in unique:
                return True
            unique.add(num)
        return False