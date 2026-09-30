class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l, r = 0, 0
        hashset = set()

        while r < len(nums):
            if (r - l) > k:
                hashset.remove(nums[l])
                l += 1

            if nums[r] in hashset:
                return True

            hashset.add(nums[r])
            r += 1
        return False
        