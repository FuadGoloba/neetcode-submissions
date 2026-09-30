class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        wdw_map = {}
        st_wdw, end_wdw, max_len = 0, 0, 0

        while end_wdw < len(s):
            wdw_map[s[end_wdw]] = wdw_map.get(s[end_wdw], 0) + 1
            
            if ((end_wdw - st_wdw + 1) - max(wdw_map.values())) > k:
                wdw_map[s[st_wdw]] -= 1
                if wdw_map[s[st_wdw]] == 0:
                    del wdw_map[s[st_wdw]]
                st_wdw += 1

            max_len = max((end_wdw - st_wdw) + 1, max_len)
            end_wdw += 1

        return max_len