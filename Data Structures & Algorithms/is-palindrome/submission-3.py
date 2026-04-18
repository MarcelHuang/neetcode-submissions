class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
            

        alphanumeric = []
        for char in s:
            if char.isalnum():
                alphanumeric.append(char.lower())
        for i, char in enumerate(alphanumeric):
            if char != alphanumeric[-i - 1]:
                return False
        return True