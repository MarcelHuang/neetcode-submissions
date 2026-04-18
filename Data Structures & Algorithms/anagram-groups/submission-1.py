class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # One liner = dictionary: char counts => list of strings
        results = collections.defaultdict(list)
        for word in strs:
            count = [0] * 26
            for char in word:
                index = ord(char) - ord("a")
                count[index] += 1
            results[tuple(count)].append(word)
        return results.values()












































        # Idea: use a dictionary to store character count => words
        results = collections.defaultdict(list)
        for string in strs:
            count = [0] * 26
            for char in string:
                index = ord(char) - ord("a")
                count[index] += 1
            results[tuple(count)].append(string)
        return results.values()