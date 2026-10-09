class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            # conditions to skip duplicate
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            target = 0 - nums[i]

            # break problem down into two sum with target
            l, r = i + 1, len(nums) - 1

            while l < r:
                # Condition for two sum making up target
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l = l + 1
                    r -= 1

                    # Check to skip duplicates
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return result
