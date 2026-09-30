class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        l, r = 0, 0
        hashset = set()

        while r < len(s):
            if s[r] not in hashset:
                hashset.add(s[r])
                max_length = max(max_length, (r-l) + 1)
                r += 1
            else:
                hashset.remove(s[l])
                l += 1
        return max_length