class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Conditions
        # Only add open parenthesis if len(open) < n
        # Only add closed parenthesis if len(closed) < len(open)
        # well-formed parentheses is when len(open) == len(closed) == n

        all_combinations = []
        stack = []

        def backtrack(open_count, closed_count):
            # Base case
            if open_count == closed_count == n:
                valid_parentheses = "".join(stack)
                all_combinations.append(valid_parentheses)

            # Condition to add open parenthesis
            if open_count < n:
                stack.append("(")
                backtrack(open_count + 1, closed_count)
                stack.pop()

            # Condition to add closed parenthesis
            if closed_count < open_count:
                stack.append(")")
                backtrack(open_count, closed_count + 1)
                stack.pop()

        backtrack(0, 0)
        return all_combinations