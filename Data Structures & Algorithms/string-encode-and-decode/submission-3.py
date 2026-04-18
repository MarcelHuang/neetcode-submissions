class Solution:

    def encode(self, strs: List[str]) -> str:
        list_of_strings = []
        for string in strs:
            list_of_strings.append(str(len(string)))
            list_of_strings.append("#")
            list_of_strings.append(string)
        return "".join(list_of_strings)


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res
