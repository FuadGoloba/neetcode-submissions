class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums1_copy = nums1[:m]
        l, r, idx = 0, 0, 0

        while r < n and l < m:
            if nums2[r] < nums1_copy[l]:
                nums1[idx] = nums2[r]
                r += 1

            else:
                nums1[idx] = nums1_copy[l]
                l += 1

            idx += 1

        while l < m:
            nums1[idx] = nums1_copy[l]
            l += 1
            idx += 1

        while r < n:
            nums1[idx] = nums2[r]
            r += 1
            idx += 1
            

        