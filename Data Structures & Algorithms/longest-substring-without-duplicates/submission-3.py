class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, max_len = 0, 0, 0
        window_map = {} # stores a map of chars to their index

        for right, char in enumerate(s):
            if char in window_map and window_map[char] >= left:
                left = window_map[char] + 1 # the new window starts at the index of the current dupe char + 1

            window_map[char] = right # insert or update the new index
            max_len = max(max_len, right - left + 1)
        
        return max_len
