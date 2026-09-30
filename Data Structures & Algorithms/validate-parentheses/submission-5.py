class Solution:
    def isValid(self, s: str) -> bool:
        openToClose = {'(':')', '[':']', '{': '}'}
        stack = []

        for p in s:
            if p in openToClose:
                stack.append(openToClose[p])
            else:
                if not stack or stack.pop() != p:
                    return False
        return True if not stack else False