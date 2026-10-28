class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 0
        longest = 0
        dupe = set()

        while end < len(s):
            while s[end] in dupe:
                dupe.remove(s[start])
                start += 1
            
            
            dupe.add(s[end])
            longest = max(longest, (end - start) + 1)
            end += 1
            
        return longest
