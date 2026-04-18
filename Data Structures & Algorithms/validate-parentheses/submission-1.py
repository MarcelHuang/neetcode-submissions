class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        opens = ["(", "{", "["]
        stack = []
        for bracket in s:
            if bracket in opens:
                stack.append(bracket)
            elif stack and stack[-1] == parentheses[bracket]:
                stack.pop()
            else:
                return False
        if not stack:
            return True
        else:
            return False