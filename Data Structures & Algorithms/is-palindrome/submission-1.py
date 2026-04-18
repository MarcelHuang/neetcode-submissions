class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = []
        for char in s:
            if char.isalnum():
                alphanumeric.append(char.lower())
        for i, char in enumerate(alphanumeric):
            if char != alphanumeric[-i - 1]:
                return False
        return True