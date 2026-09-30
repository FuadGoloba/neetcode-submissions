class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        left_idx, right_idx = 0, len(s) - 1
        temp = ''
        while left_idx < right_idx:
            temp = s[left_idx]
            s[left_idx] = s[right_idx]
            s[right_idx] = temp

            left_idx += 1
            right_idx -= 1
        
        return s
        