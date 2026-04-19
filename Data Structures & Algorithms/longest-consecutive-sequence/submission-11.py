class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Start counting when we find the beginning of a consecutive sequence
        # A number is the start of the sequence if (num - 1) not in the set
        numSet = set(nums)
        longest = 0
        for num in nums:
            if (num - 1) not in numSet:  # start of seq
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest