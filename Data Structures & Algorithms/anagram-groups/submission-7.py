class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # count the character to be used as a hashmap for each word
        results = defaultdict(list)  # count as key => ["str1", "str2"]
        for word in strs:
            count = [0] * 26
            for char in word:
                position = ord(char) - ord('a')
                count[position] += 1
            # key = ','.join(str(c) for c in count)
            # results[key].append(word)
            results[tuple(count)].append(word)
        return list(results.values())