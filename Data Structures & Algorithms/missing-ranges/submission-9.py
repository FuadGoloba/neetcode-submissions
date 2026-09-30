class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        result = []
        l, r, n = 0, 1, len(nums)

        if n == 0:
            return [[lower, upper]]

        if nums[0] > lower:
            result.append([lower, nums[0] - 1])

        while r < n:
            if nums[r] - nums[l] > 1:
                result.append([nums[l] + 1, nums[r] - 1])
            
            l += 1
            r += 1

        if upper - nums[n - 1] > 0:
            result.append([nums[n - 1] + 1, upper])

        return result