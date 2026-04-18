class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Intuition: vertically scanning through the first word and check the length with index
        results = []
        first_word = strs[0]
        for i, char in enumerate(first_word):
            for word in strs:
                if i == len(word) or word[i] != char:
                    return "".join(results)
            results.append(char)
        return "".join(results)
                