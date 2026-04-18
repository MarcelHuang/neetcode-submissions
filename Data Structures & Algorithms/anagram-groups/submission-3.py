class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # One liner = dictionary: char counts => list of strings
        # 1. initiate results with defaultdict list
        # 2. Loop through strings
        # 3. Loop through char and count it
        # 4. store in a tuple
        # 5. return the list
        results = collections.defaultdict(list)
        for string in strs:
            count = [0] * 26  # a-z => count
            for char in string:
                index = ord(char) - ord('a')
                count[index] += 1
            key = tuple(count)
            results[key].append(string)
        return results.values()






































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