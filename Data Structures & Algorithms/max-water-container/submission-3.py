class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = 0

        while l < r:
            # calculate the area that maximises the width and height
            area = (r - l) * min(heights[r],heights[l])
            max_area = max(max_area, area)

            # condition to find the max height while maximising width
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_area

