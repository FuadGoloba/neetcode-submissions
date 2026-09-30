class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        min_length = min(len(word1), len(word2))
        new_string = ''
        for idx in range(min_length):
            new_string += word1[idx] + word2[idx]

        if len(word1) > min_length:
            new_string += word1[min_length::]
        if len(word2) > min_length:
            new_string += word2[min_length::]
        
        return new_string
        