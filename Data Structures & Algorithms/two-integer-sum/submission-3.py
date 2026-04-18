class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Sorting => Two pointers
        A = []
        for i, num in enumerate(nums):
            A.append([num, i])
        A.sort()
        left = 0
        right = len(nums) - 1
        while left < right:
            current_sum = A[left][0] + A[right][0]
            if current_sum == target:
                left_index = min(A[left][1], A[right][1])
                right_index = max(A[left][1], A[right][1])
                return [left_index, right_index]
            elif current_sum < target:
                left += 1
            else:
                right -= 1


