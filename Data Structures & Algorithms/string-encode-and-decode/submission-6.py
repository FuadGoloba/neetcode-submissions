class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for string in strs:
            encoded.append(str(len(string)))
            encoded.append('#')
            encoded.append(string)
        return "".join(encoded)
        
    def decode(self, s: str) -> List[str]:
        curr = 0
        decoded = []

        while curr < len(s):
            # initialise start of delimiter
            delimiter = curr
            # Find the delimiter position
            while s[delimiter] != '#':
                delimiter += 1 
                
            # find length of word
            length = int(s[curr: delimiter])
            word_start = delimiter + 1

            word = s[word_start: word_start + length]
            decoded.append(word)
            curr = word_start + length

        return decoded