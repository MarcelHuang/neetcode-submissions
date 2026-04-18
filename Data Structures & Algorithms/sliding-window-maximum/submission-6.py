class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()
        left = 0
        for right in range(len(nums)):
            # 1. pop if not smaller
            while q and nums[right] > nums[q[-1]]:
                q.pop()
            # 2. append to q
            q.append(right)
            # 3. slide left and right
            if left > q[0]:
                q.popleft()
            if (right + 1) >= k:
                output.append(nums[q[0]])
                left += 1
        return output