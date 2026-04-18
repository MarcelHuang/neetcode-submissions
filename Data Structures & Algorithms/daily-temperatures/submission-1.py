class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Initialize result array with 0s - default case when no warmer temperature is found
        # Length matches input array since we need an answer for each day
        res = [0] * len(temperatures)
        
        # Stack will store pairs of (temperature, index)
        # Using a monotonic decreasing stack pattern
        # We only keep temperatures in decreasing order
        stack = []
        
        # Iterate through each temperature with its index
        for i, curr_temp in enumerate(temperatures):
            # While stack has elements AND current temperature is warmer than top of stack
            # We've found a warmer day for all temperatures in stack that are colder
            while stack and curr_temp > stack[-1][0]:
                # Get the previous temperature and its index from stack
                prev_temp, prev_idx = stack.pop()
                
                # Calculate number of days between current warmer temp and previous temp
                # Store it in result array at the index of the colder temperature
                res[prev_idx] = i - prev_idx
            
            # Add current temperature and index to stack
            # It will be processed when we find a warmer temperature later
            stack.append((curr_temp, i))
            
        return res