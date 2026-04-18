class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        count = 0
        for right in range(len(nums)):
            if nums[right] != val:
                count += 1
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        return count