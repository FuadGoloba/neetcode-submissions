class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        def _reverse(nums, l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1

        _reverse(nums, 0, n - 1)
        _reverse(nums, 0, k - 1)
        _reverse(nums, k, n - 1)
