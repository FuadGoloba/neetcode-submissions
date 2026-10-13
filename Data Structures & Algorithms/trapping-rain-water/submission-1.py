class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0] * len(height)
        max_right = [0] * len(height)
        total = 0

        max_left[0] = height[0]
        for l in range(1, len(height)):
            max_left[l]= max(height[l-1], max_left[l-1])

        max_right[-1] = height[-1]
        for r in range(len(height)-2, -1, -1):
            max_right[r] = max(height[r+1], max_right[r+1])

        for i in range(len(height)):
            trapped = min(max_left[i], max_right[i]) - height[i]
            if trapped > 0:
                total += trapped

        return total