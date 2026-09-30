class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_copy = nums1[:m]
        l, r, curr_idx = 0, 0, 0

        while l < m and r < n:
            if nums1_copy[l] < nums2[r]:
                nums1[curr_idx] = nums1_copy[l]
                l += 1
            else:
                nums1[curr_idx] = nums2[r]
                r += 1
            curr_idx += 1

        if l < m:
            nums1[curr_idx:] = nums1_copy[l:]
        
        if r < n:
            nums1[curr_idx:] = nums2[r:]