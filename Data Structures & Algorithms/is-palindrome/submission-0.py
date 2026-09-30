class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for char in s:
            if (
                ord('a') <= ord(char) <= ord('z') or
                ord('A') <= ord(char) <= ord('Z') or
                ord('0') <= ord(char) <= ord('9')
            ):
                new_s += char.lower()

        l,r = 0, len(new_s) - 1

        while l < r:
            if new_s[l] != new_s[r]:
                return False
            l += 1
            r -= 1
        return True
        