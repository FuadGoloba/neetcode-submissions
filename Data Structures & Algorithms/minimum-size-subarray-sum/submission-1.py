class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window_start, window_end = 0, 0
        total_window = 0
        min_length = len(nums) + 1

        while window_end < len(nums):
            total_window += nums[window_end]
            while total_window >= target:
                min_length = min((window_end - window_start) + 1, min_length)
                total_window -= nums[window_start]
                window_start += 1
            window_end += 1
        return 0 if min_length > len(nums) else min_length
