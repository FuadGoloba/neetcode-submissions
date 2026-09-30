class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}
        for i, num in enumerate(nums):
            remainder = target - num
            if remainder in seen:
                return [i, seen[remainder]] if i < seen[remainder] else [seen[remainder], i]
            seen[num] = i
        