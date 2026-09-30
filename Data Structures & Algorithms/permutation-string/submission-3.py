class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map, s2_map = {}, {}

        if len(s1) > len(s2):
            return False

        for char in s1:
            s1_map[char] = s1_map.get(char, 0) + 1

        left, right = 0, 0
        while right < len(s2):
            s2_map[s2[right]] = s2_map.get(s2[right], 0) + 1
            if (right - left) + 1 > len(s1):
                s2_map[s2[left]] -= 1
                if s2_map[s2[left]] == 0:
                    del s2_map[s2[left]]

                left += 1
            
            if s1_map == s2_map:
                return True
            right += 1

        return False