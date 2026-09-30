class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        alpha_count_s, alpha_count_t = [0] * 26, [0] * 26

        for i in range(len(s)):
            alpha_count_s[ ord(s[i]) - ord('a') ] += 1
            alpha_count_t[ ord(t[i]) - ord('a') ] += 1

        return alpha_count_s == alpha_count_t