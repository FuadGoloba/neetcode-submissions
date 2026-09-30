class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                del_left = s[left + 1 : right + 1] # delete left end from string
                del_right = s[left : right] # delete right end from string

                return (del_left == del_left[::-1] or del_right == del_right[::-1]) # check if they are palindromic after deletion form either end
        
            left, right = left + 1, right - 1
        return True

            

