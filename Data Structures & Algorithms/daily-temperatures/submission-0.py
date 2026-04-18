class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Given an array of daily temperatures, returns an array where each element
        represents how many days you need to wait until a warmer temperature.
        If no warmer temperature exists, the result will be 0 for that day.
        
        This is an optimized solution that processes temperatures from right to left,
        using previous results to skip unnecessary comparisons.
        
        Example:
        temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
        output =       [1,  1,  4,  2,  1,  1,  0,  0]
                      ^                          ^
                      |                          |
        Wait 1 day    |                       No warmer day exists
        for 74 (warmer)
        
        Args:
            temperatures: List[int] - Daily temperatures
            
        Returns:
            List[int] - Number of days to wait for a warmer temperature
            
        Time Complexity: O(n) - Each element is visited at most once due to skipping
        Space Complexity: O(1) - Only output array is used
        """
        n = len(temperatures)
        # Initialize result array with zeros
        # Zero means no warmer temperature will be found
        res = [0] * n
        
        # Process temperatures from right to left
        # Start from second-to-last element (n-2) down to first element (0)
        for i in range(n - 2, -1, -1):
            # Start checking the next day
            j = i + 1
            
            # Keep looking for warmer temperature
            while j < n and temperatures[j] <= temperatures[i]:
                # If we hit a day with no warmer temperature ahead (res[j] == 0),
                # then there's no point continuing - we won't find warmer temperature
                if res[j] == 0:
                    j = n  # Force exit by setting j to end of array
                    break
                
                # The clever optimization: instead of checking each day,
                # jump ahead by the pre-computed result for the current day
                # This skips days we know won't be warmer
                j += res[j]
            
            # If we found a warmer temperature (j < n),
            # calculate how many days we need to wait
            if j < n:
                res[i] = j - i
        
        return res