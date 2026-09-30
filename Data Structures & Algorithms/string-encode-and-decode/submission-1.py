class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for st in strs:
            s += str(len(st)) + '#' + st
        return s

    def decode(self, s: str) -> List[str]:
        res, curr_idx = [], 0

        while curr_idx < len(s):
            delimiter_idx = curr_idx

            while s[delimiter_idx] != '#':
                delimiter_idx += 1

            word_length = int(s[curr_idx : delimiter_idx])
            curr_idx = delimiter_idx + 1
            #delimiter_idx = curr_idx + word_length
            res.append(s[curr_idx : curr_idx + word_length])

            curr_idx = curr_idx + word_length

        return res




