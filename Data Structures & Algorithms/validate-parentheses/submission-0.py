class Solution:
    def isValid(self, s: str) -> bool:
        closed_brkts = {')': '(', ']': '[', '}':'{'}

        stack = []

        for brkt in s:
            if brkt not in closed_brkts:
                stack.append(brkt)
            else:
                if stack and stack[-1] == closed_brkts[brkt]:
                    stack.pop()
                else:
                    return False

        return True if not stack else False