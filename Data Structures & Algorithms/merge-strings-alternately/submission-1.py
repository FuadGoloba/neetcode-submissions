class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_length = min(len(word1), len(word2))
        new_string = []
        for idx in range(min_length):
            new_string.append(word1[idx])
            new_string.append(word2[idx])

        if len(word1) > min_length:
            new_string.append(word1[min_length:])
        if len(word2) > min_length:
            new_string.append(word2[min_length:])
        
        return ''.join(new_string)
        