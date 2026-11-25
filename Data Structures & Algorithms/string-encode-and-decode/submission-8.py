class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""

        for s in strs:
            encoded_str += str(len(s)) + "#" + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        curr = 0
        decoded_str = []

        while curr < len(s):
            # get delimiter #
            dlmtr = curr
            while s[dlmtr] != "#":
                dlmtr += 1
            # get length
            s_len = int(s[curr:dlmtr])
            start = dlmtr + 1
            end = start + s_len

            # get string
            string = s[start : end]
            decoded_str.append(string)

            curr = end
        return decoded_str


            