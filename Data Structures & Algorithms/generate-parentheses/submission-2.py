class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Generates all combinations of well-formed parentheses for a given number of pairs.
        
        A well-formed parentheses string must:
        1. Have equal numbers of open and closed parentheses
        2. At any point while reading from left to right, the number of open parentheses
           must be >= the number of closed parentheses
        
        Example:
        n = 2 -> ["(())", "()()"]
        n = 3 -> ["((()))", "(()())", "(())()", "()(())", "()()()"]
        
        Args:
            n: int - Number of pairs of parentheses to generate
            
        Returns:
            List[str] - All possible valid combinations
            
        Time Complexity: O(4^n / sqrt(n)) - Catalan number sequence
        Space Complexity: O(n) for recursion depth
        """
        stack = []      # Current parentheses combination being built
        results = []    # List to store all valid combinations
        
        def backtrack(openN: int, closedN: int) -> None:
            """
            Recursive backtracking function to generate valid combinations.
            
            Args:
                openN: Number of open parentheses used so far
                closedN: Number of closed parentheses used so far
            """
            # Base case: if we've used n open and n closed parentheses,
            # we have a valid combination
            if openN == closedN == n:
                results.append("".join(stack))
                return
            
            # We can add an open parenthesis if we haven't used all n
            if openN < n:
                stack.append("(")                    # Add open parenthesis
                backtrack(openN + 1, closedN)        # Recurse with one more open
                stack.pop()                          # Backtrack by removing it
            
            # We can add a closing parenthesis if we have more open than closed
            if closedN < openN:                      # This ensures valid combinations
                stack.append(")")                    # Add closing parenthesis
                backtrack(openN, closedN + 1)        # Recurse with one more closed
                stack.pop()                          # Backtrack by removing it
        
        # Start the backtracking with 0 open and 0 closed parentheses
        backtrack(0, 0)
        return results