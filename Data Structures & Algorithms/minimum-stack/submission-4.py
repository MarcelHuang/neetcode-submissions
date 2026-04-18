class MinStack:
    def __init__(self):
        """
        Initialize your data structure here.
        min: tracks current minimum value
        stack: stores differences between values and current minimum
        """
        self.min = float('inf')
        self.stack = []
        
    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        For first element, store 0 and set as minimum.
        For subsequent elements, store difference with current minimum.
        Update minimum if new value is smaller.
        """
        if not self.stack:
            self.stack.append(0)
            self.min = x
        else:
            self.stack.append(x - self.min)
            if x < self.min:
                self.min = x
    
    def pop(self) -> None:
        """
        Removes the element on top of the stack.
        If popped difference is negative, restore previous minimum.
        """
        if not self.stack:
            return
        
        pop = self.stack.pop()
        
        if pop < 0:
            self.min = self.min - pop
            
    def top(self) -> int:
        """
        Get the top element.
        If stored difference > 0: actual value = difference + minimum
        If stored difference ≤ 0: minimum is the actual value
        """
        top = self.stack[-1]
        if top > 0:
            return top + self.min
        else:
            return self.min
    
    def getMin(self) -> int:
        """
        Retrieve the minimum element in the stack.
        """
        return self.min

# Example usage:
"""
stack = MinStack()
stack.push(3)    # stack=[0], min=3
stack.push(5)    # stack=[0, 2], min=3
stack.push(2)    # stack=[0, 2, -1], min=2
stack.pop()      # stack=[0, 2], min=3
print(stack.top())    # Returns 5
print(stack.getMin()) # Returns 3
"""