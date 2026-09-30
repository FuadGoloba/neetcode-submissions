class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        result = []
        l, r = 0, 1

        nums_copy = nums[:]
        nums_copy.insert(0, lower - 1)

        while r < len(nums_copy):
            if nums_copy[r] - nums_copy[l] > 1:
                result.append([nums_copy[l] + 1, nums_copy[r] - 1])
            l += 1
            r += 1

        if upper - nums_copy[l] > 0:
            result.append([nums_copy[l] + 1, upper])

        return result