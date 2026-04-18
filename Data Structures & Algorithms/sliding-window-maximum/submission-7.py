class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()
        left = 0
        for right in range(len(nums)):
            # 1. pop if
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            # 2. append to deque
            q.append(right)
            # 3. slide
            if q[0] < left:
                q.popleft()
            if (right + 1) >= k:
                output.append(nums[q[0]])
                left += 1
        return output