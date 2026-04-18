class Solution:
    def isValid(self, s: str) -> bool:
        """
        Determines if a string of parentheses is valid.
        A string is valid if:
        1. Open brackets must be closed by the same type of brackets
        2. Open brackets must be closed in the correct order
        3. Every close bracket has a corresponding open bracket
        
        Examples:
        - "()[]{}" -> True
        - "([)]"   -> False
        - "]"      -> False
        
        Args:
            s: str - String containing only parentheses characters: '(', ')', '{', '}', '[', ']'
            
        Returns:
            bool - True if string is valid, False otherwise
            
        Time Complexity: O(n) where n is the length of string
        Space Complexity: O(n) for the stack
        """
        # Dictionary mapping closing brackets to their corresponding opening brackets
        # This makes it easy to check if brackets match
        parentheses = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        
        # Set of opening brackets for quick lookup
        # Using set instead of list for O(1) lookup time
        opens = set(["(", "{", "["])
        
        # Stack to keep track of opening brackets
        stack = []
        
        # Process each bracket in the string
        for bracket in s:
            if bracket in opens:
                # If it's an opening bracket, push onto stack
                stack.append(bracket)
            elif bracket in parentheses:  # If it's a closing bracket
                # Three conditions must be met for valid closing bracket:
                # 1. Stack must not be empty (needs matching open bracket)
                # 2. Top of stack must match current bracket
                if stack and stack[-1] == parentheses[bracket]:
                    stack.pop()  # Remove the matching opening bracket
                else:
                    # Invalid cases:
                    # - Stack is empty (no matching open bracket)
                    # - Top of stack doesn't match (wrong order)
                    return False
        
        # After processing all brackets:
        # - Stack should be empty for valid string
        # - If stack not empty, we have unmatched opening brackets
        return len(stack) == 0  # Simplified from if/else