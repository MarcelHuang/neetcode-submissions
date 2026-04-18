class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Initialize result array and deque (will store indices)
        output = []
        q = deque()
        
        # Initialize window pointers
        l = r = 0
        
        # Process all elements in the array
        for r in range(len(nums)):
            # STEP 1: Remove all elements smaller than current element from back of deque
            # This maintains decreasing monotonic sequence (largest elements first)
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            # STEP 2: Add current element's index to deque
            q.append(r)
            
            # STEP 3: Remove element from front if it's outside current window
            # If left pointer has moved past the leftmost element in deque
            if l > q[0]:
                q.popleft()
            
            # STEP 4: If we have a full window (k elements), add to result
            if (r + 1) >= k:
                # Front of deque always has max element's index
                output.append(nums[q[0]])
                # Move left pointer to slide window
                l += 1
        return output

"""
Key Points:
1. Deque stores indices, not values, to track window boundaries
2. Deque maintains decreasing order of values (using their indices)
3. Front of deque (q[0]) always has index of current window's maximum
4. Window size is maintained by incrementing l and checking q[0]

Example:
nums = [1,3,-1,-3,5,3,6,7], k = 3

For window [1,3,-1]:
- Initially q gets 1's index
- When 3 comes, removes 1's index (smaller)
- When -1 comes, keeps 3's index (larger)
- Max is 3

Time: O(n) - each element pushed/popped at most once
Space: O(k) - deque stores at most k elements
"""