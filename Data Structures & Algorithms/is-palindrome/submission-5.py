class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        def alphaNum(char):
            return (
                ord('A') <= ord(char) <= ord('Z') or
                ord('a') <= ord(char) <= ord('z') or
                ord('0') <= ord(char) <= ord('9')
            )

        while left < right:
            # check if chars are alphanum
            while not alphaNum(s[left]) and left < right:
                left += 1
            while not alphaNum(s[right]) and left < right:
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True