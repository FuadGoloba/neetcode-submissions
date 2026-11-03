class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqMap = {} # maps chars to their freq to track repeated count for replacement
        start = 0 # start of a window
        maxLen = 0

        for end in range(len(s)):
            # add char and freq to freqMap
            freqMap[s[end]] = freqMap.get(s[end], 0) + 1

            # if we exceed the k count to replace
            if (end - start + 1) - max(freqMap.values()) > k:
                # we start at a new window
                freqMap[s[start]] -= 1
                start += 1

            maxLen = max(maxLen, (end - start + 1))

        return maxLen

        