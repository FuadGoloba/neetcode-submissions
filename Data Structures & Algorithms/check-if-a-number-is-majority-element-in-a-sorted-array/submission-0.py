class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        
        freq = 0

        for num in nums:
            if num == target:
                freq += 1
        return freq > len(nums) / 2