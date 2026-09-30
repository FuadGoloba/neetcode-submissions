class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st_wdw, end_wdw, max_len = 0, 0, 0
        window = set()

        while end_wdw < len(s):
            if s[end_wdw] in window:
                window.remove(s[st_wdw])
                st_wdw += 1
            else:
                window.add(s[end_wdw])
                max_len = max(max_len, (end_wdw - st_wdw) + 1)
                end_wdw += 1
        return max_len