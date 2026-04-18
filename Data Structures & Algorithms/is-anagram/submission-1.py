class Solution:
    # O(s log s) + O(t log t) time, where s and t are the number of characters
    # in s and t respectively
    # O(1) extra space (with some sorting library)
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)