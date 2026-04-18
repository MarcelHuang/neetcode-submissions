class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = [0] * len(temperatures)
        stack = []  # pair: (index, temperature)
        for index, temperature in enumerate(temperatures):
            while stack and stack[-1][1] < temperature:
                stack_index, stack_temperature = stack.pop()
                days_diff = index - stack_index
                days[stack_index] = days_diff
            stack.append((index, temperature))
        return days