class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1Arr, s2Arr = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1Arr[ord(s1[i]) - ord('a')] += 1
            s2Arr[ord(s2[i]) - ord('a')] += 1

        start = 0
        for end in range(len(s1), len(s2)):
            if s1Arr == s2Arr:
                return True

            s2Arr[ord(s2[start]) - ord('a')] -= 1
            s2Arr[ord(s2[end]) - ord('a')] += 1
            start += 1

        return s1Arr == s2Arr