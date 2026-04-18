class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute force
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        previous_map = {}  # storing value -> index
        for i, n in enumerate(nums):
            difference = target - n
            if difference in previous_map:
                return [previous_map[difference], i]
            previous_map[n] = i

