class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        l, r = 0, 0
        max_len = 0
        max_freq = 0

        while r < len(s):
            hashmap[s[r]] = hashmap.get(s[r], 0) + 1
            max_freq = max(max_freq, hashmap[s[r]])
            if (r - l + 1) - max_freq <= k:
                max_len = max(max_len, r - l + 1)
            else:
                hashmap[s[l]] = hashmap[s[l]] - 1
                l += 1
            r += 1
        return max_len