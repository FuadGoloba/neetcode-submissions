class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr_s = [0] * 26
        arr_t = [0] * 26

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            arr_s[ord(s[i]) - ord('a')] += 1
            arr_t[ord(t[i]) - ord('a')] += 1

        return arr_s == arr_t