class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        res = 0
        for num in nums:
            streak = 0
            curr = num
            while curr in numset:
                streak += 1
                curr += 1
            res = max(res, streak)
        return res