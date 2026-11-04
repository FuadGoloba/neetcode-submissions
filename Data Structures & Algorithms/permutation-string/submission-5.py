class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1Map, s2Map = {}, {}

        for i in range(len(s1)):
            s1Map[s1[i]] = s1Map.get(s1[i], 0) + 1
            s2Map[s2[i]] = s2Map.get(s2[i], 0) + 1

        start = 0
        for end in range(len(s1), len(s2)):
            if s1Map == s2Map:
                return True

            # shrink window
            if s2Map[s2[start]] > 1:
                s2Map[s2[start]] -= 1
            else:
                del s2Map[s2[start]]
            
            s2Map[s2[end]] = s2Map.get(s2[end], 0) + 1
            start += 1

        return s1Map == s2Map