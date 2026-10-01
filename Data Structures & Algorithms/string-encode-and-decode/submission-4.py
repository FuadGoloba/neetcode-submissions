class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for word in strs:
            # encode a string using the string length and a delimiter to identify the string
            encoded_str = encoded_str + str(len(word)) + "#" + word
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        curr_ptr = 0

        while curr_ptr < len(s):
            delimiter_ptr = curr_ptr
            # Find the delimiter # which denotes the start of a string
            while s[delimiter_ptr] != "#":
                delimiter_ptr += 1
            # Find the string length which comes before the delimiter
            str_len = int(s[curr_ptr:delimiter_ptr])
            word_start_ptr = delimiter_ptr + 1 # index of start of the string
            decoded_strs.append(s[word_start_ptr: word_start_ptr + str_len])
            curr_ptr = word_start_ptr + str_len # update curr ptr to the start of the next encoded string (i.e 3#cat)
        
        return decoded_strs

            