class Solution:
    # O(n log n) time, where n is the longest between s and t
    # O(1) extra space
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        if s == t:
            return True
        else:
            return False