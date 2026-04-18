class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = 0
        stack = []
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                stack.append(- stack.pop() + stack.pop())
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                divisor = stack.pop()
                divident = stack.pop()
                stack.append(int(divident / divisor))
            else:
                stack.append(int(token))
        return stack[0]