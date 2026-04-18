class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # track nums with hashmap value:index
        prevMap = {}  # diff:index
        for i, num in enumerate(nums):
            diff = target - num
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[num] = i