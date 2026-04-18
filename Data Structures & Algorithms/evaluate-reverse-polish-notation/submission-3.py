class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Evaluates an arithmetic expression in Reverse Polish Notation (RPN).
        
        RPN is a postfix notation where operators follow their operands.
        Example: ["2", "1", "+", "3", "*"] represents (2 + 1) * 3 = 9
        
        Args:
            tokens: List[str] - Array of strings representing numbers and operators (+, -, *, /)
        
        Returns:
            int - Result of evaluating the RPN expression
        
        Time Complexity: O(n) where n is the length of tokens
        Space Complexity: O(n) in worst case for the stack
        """
        stack = []  # Stack to keep track of operands
        
        for token in tokens:
            if token in {"+", "-", "*", "/"}:  # If token is an operator
                # Pop the last two numbers from stack
                # Note: Order matters for - and / operations
                num2 = stack.pop()  # Second operand
                num1 = stack.pop()  # First operand
                
                # Perform the operation based on the operator
                if token == "+":
                    stack.append(num1 + num2)
                elif token == "-":
                    stack.append(num1 - num2)  # num1 - num2, not num2 - num1
                elif token == "*":
                    stack.append(num1 * num2)
                elif token == "/":
                    # Handle division according to problem requirements:
                    # - Truncate toward zero
                    # - Assume division by zero is not possible
                    stack.append(int(num1 / num2))
            else:
                # If token is a number, convert to integer and push to stack
                stack.append(int(token))
        
        # The final answer will be the only number left in the stack
        return stack[0]