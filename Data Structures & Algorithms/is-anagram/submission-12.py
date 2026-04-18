class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # Fixed Hash
        count = [0] * 26
        for char in s:
            position = ord(char) - ord('a')
            count[position] += 1
        for char in t:
            position = ord(char) - ord('a')
            count[position] -= 1
        for val in count:
            if val != 0:
                return False
        return True
        