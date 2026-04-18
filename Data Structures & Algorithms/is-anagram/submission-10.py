class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Idea: if each character count is the same, it is an anagram
        # otherwise, not an anagram
        # first check the length, if different, not an anagram
        if len(s) != len(t):
            return False
        #initialize count s and count t
        count_s = {}
        count_t = {}
        # iterate s, and t, and count each character for s and t
        # Because now we know it's the same length, we can iterate through either s or t
        for i in range(len(s)):
            char_s, char_t = s[i], t[i]
            count_s[char_s] = 1 + count_s.get(char_s, 0)
            count_t[char_t] = 1 + count_t.get(char_t, 0)
        return count_s == count_t
        # compare the count in the end to return an anagram or not