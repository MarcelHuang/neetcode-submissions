class MinStack:
    # Idea: Store differences between values
    def __init__(self):
        self.min = float('inf')  # initialize minimum to infinitiy
        self.stack = []          # Empty stack to store differences

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)  # First element: store 0 as difference
            self.min = val   # Set first element as minimum
        else:
            difference = val - self.min
            self.stack.append(difference)  # store difference with current minimum
            if val < self.min:
                self.min = val  # Update minimum if new value is smaller
        

    def pop(self) -> None:
        if not self.stack:
            return
        
        pop = self.stack.pop()

        if pop < 0:                     # if popped difference is negative
            self.min = self.min - pop   # Restore previous minimum

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return top + self.min  # Actual value = difference + minimum
        else:
            return self.min  # If difference is <= 0, minimum is the actual value
        

    def getMin(self) -> int:
        return self.min
