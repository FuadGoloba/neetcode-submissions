class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        countT, window = {}, {}
        # Get the count of each char in t
        for char in t:
            countT[char] = countT.get(char, 0) + 1

        have = 0
        need = len(countT)
        l = 0
        resLen, resPos = float('inf'), [-1, -1]
        for r, char in enumerate(s):
            # add each char from s into window
            window[char] = window.get(char, 0) + 1

            # Check that our window has added a character needed from t
            if char in countT and countT[char] == window[char]:
                have += 1

            while have == need:
                # shrink our window till we get the shortest substring
                if (r - l + 1) < resLen:
                    resLen = (r - l + 1)
                    resPos = [l, r]

                # pop from the window
                window[s[l]] -= 1

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1

                l += 1

        return s[resPos[0]:resPos[1] + 1] if resLen != float('inf') else ""

            