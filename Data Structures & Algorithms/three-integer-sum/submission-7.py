class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()

        for i in range(len(nums)):
            # conditions to skip duplicate
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = 0 - nums[i]

            # break problem down into two sum with target using hashset
            seen = set()

            for j in range(i + 1, len(nums)):
                remainder = target - nums[j]
                if remainder in seen:
                    result.add((nums[i], nums[j], remainder))
                else:
                    seen.add(nums[j])

        return [list(triplet) for triplet in result]
