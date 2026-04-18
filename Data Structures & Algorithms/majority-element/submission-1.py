class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        for num in count:
            if count[num] > len(nums) // 2:
                return num