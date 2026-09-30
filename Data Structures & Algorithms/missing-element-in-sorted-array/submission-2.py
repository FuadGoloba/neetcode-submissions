class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        l, r = 0, 1

        while r < len(nums):
            m = nums[r] - nums[l] - 1
            if m < k:
                k -= m
            elif m >= k:
                return nums[l] + k
            l += 1
            r += 1
        
        return nums[l] + k