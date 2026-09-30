class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}
        for idx, val in enumerate(nums):
            remainder = target - val
            if remainder in seen:
                return [seen[remainder], idx]
            else:
                seen[nums[idx]] = idx