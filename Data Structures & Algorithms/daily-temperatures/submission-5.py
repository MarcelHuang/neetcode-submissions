class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        stack = []  # (index, temperature)
        for index, temperature in enumerate(temperatures):
            while stack and stack[-1][1] < temperature:  # warmer
                stack_index, stack_temperature = stack.pop()
                days = index - stack_index
                results[stack_index] = days
            stack.append((index, temperature))
        return results