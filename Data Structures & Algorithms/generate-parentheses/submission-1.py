from typing import List, Set
from dataclasses import dataclass

@dataclass
class ParenthesesState:
    """Represents the current state of parentheses generation.
    
    Attributes:
        open_count: Number of open parentheses used
        close_count: Number of closed parentheses used
        current_combination: List of current parentheses being built
    """
    open_count: int
    close_count: int
    current_combination: List[str]

class ParenthesesGenerator:
    """Generates all valid combinations of parentheses for a given number."""
    
    def __init__(self, pair_count: int):
        """Initialize the generator with the number of parentheses pairs.
        
        Args:
            pair_count: Number of pairs of parentheses to generate
            
        Raises:
            ValueError: If pair_count is negative
        """
        if pair_count < 0:
            raise ValueError("Number of parentheses pairs must be non-negative")
        self._pair_count = pair_count
        self._results: Set[str] = set()

    def _backtrack(self, state: ParenthesesState) -> None:
        """Recursively generates valid parentheses combinations.
        
        Args:
            state: Current state of the parentheses generation
        """
        # Base case: if we've used all parentheses pairs
        if state.open_count == state.close_count == self._pair_count:
            self._results.add("".join(state.current_combination))
            return

        # Add open parenthesis if we haven't used all
        if state.open_count < self._pair_count:
            state.current_combination.append("(")
            self._backtrack(ParenthesesState(
                state.open_count + 1,
                state.close_count,
                state.current_combination
            ))
            state.current_combination.pop()

        # Add closing parenthesis if it's valid
        if state.close_count < state.open_count:
            state.current_combination.append(")")
            self._backtrack(ParenthesesState(
                state.open_count,
                state.close_count + 1,
                state.current_combination
            ))
            state.current_combination.pop()

    def generate(self) -> List[str]:
        """Generates all valid combinations of parentheses.
        
        Returns:
            List of all valid parentheses combinations
            
        Example:
            >>> generator = ParenthesesGenerator(2)
            >>> result = generator.generate()
            >>> sorted(result)
            ['(())', '()()']
        """
        initial_state = ParenthesesState(0, 0, [])
        self._backtrack(initial_state)
        return sorted(list(self._results))


class Solution:
    """LeetCode solution class for generating valid parentheses combinations."""
    
    def generateParenthesis(self, n: int) -> List[str]:
        """Generate all valid parentheses combinations.
        
        Args:
            n: Number of parentheses pairs to generate
            
        Returns:
            List of all valid parentheses combinations
            
        Raises:
            ValueError: If n is negative
        """
        generator = ParenthesesGenerator(n)
        return generator.generate()