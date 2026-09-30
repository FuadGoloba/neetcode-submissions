class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map, s2_map = [0] * 26, [0] * 26

        if len(s1) > len(s2):
            return False

        for idx in range(len(s1)):
            s1_map[ord(s1[idx]) - ord('a')] += 1
            s2_map[ord(s2[idx]) - ord('a')] += 1

        for r in range(len(s1), len(s2)):
            if s1_map == s2_map:
                return True
            # remove leftmost character
            s2_map[ord(s2[r - len(s1)]) - ord('a')] -= 1
            
            # Add the next character
            s2_map[ord(s2[r]) - ord('a')] += 1

        return s1_map == s2_map

