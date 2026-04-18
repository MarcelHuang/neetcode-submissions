class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # array => set
        # loop through set
        # check if start of sequence
        # loop until sequence breaks
        # calculate longest
        numSet = set(nums)
        longest = 0
        for num in numSet:
            # if start of sequence
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest






        # 0. Convert input array to set
        numSet = set(nums)
        # 1. Initialize longest, return longest at the end
        longest = 0
        # 2. Loop through the set
        for n in numSet:
        # 3. check if it's the start of a sequence
            if (n - 1) not in numSet:
        # 4. keep incrementing length and checking the numset until n + 1 not in set
                length = 1
                while (n + length) in numSet:
                    length += 1
        # 5. compare longest with current streak and return
                longest = max(length, longest)
        return longest

        numSet = set(nums)
        longest = 0
        for n in numSet:
            # check if it's the start of a sequence
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest