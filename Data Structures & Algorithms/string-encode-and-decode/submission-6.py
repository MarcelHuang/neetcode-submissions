class Solution:
    # Idea: Length + Hashtag + string
    def encode(self, strs: List[str]) -> str:
        encoded_string = []
        for string in strs:
            encoded_string.append(str(len(string)))
            encoded_string.append("#")
            encoded_string.append(string)
        return "".join(encoded_string)

    def decode(self, s: str) -> List[str]:
        # parse the int, skip the hashtag
        decoded_string = []
        i = 0
        j = 0
        # "4#neet4#code4#love3#you"
        #    i
        #        j
        while i < len(s):
            while s[j] != "#":
                j += 1
            length = int(s[i:j])  #4
            # get the actual string based on the length by moving the pointers
            i = j + 1
            j = i + length
            string = s[i:j]
            decoded_string.append(string)
            i = j
        return decoded_string
