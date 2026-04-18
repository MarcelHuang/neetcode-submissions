class Solution:
    # O(s log s) + O(t log t) time, where s and t are the number of characters
    # in s and t respectively
    # O(1) extra space (with some sorting library)
    # def isAnagram(self, s: str, t: str) -> bool:
    #     return sorted(s) == sorted(t)

    # O(3s) time which reduces to O(s)
    # Because we already do the initial checking of comparing both length of the string
    # the rest would be iteration of the same length of string
    # O(2s) space as we're storing a dictionary
    # Example: "abcde" will be space of 5
    def isAnagram(self, s: str, t: str) -> bool:
        # Pythonic one-liner solution
        # return Counter(s) == Counter(t)
        if len(s) != len(t):
            return False
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT