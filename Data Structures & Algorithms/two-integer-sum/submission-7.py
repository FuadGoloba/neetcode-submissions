class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}
        for i, num in enumerate(nums):
            remainder = target - num
            if remainder in seen:
                return [min(i, seen[remainder]), max(i, seen[remainder])]
            seen[num] = i
        