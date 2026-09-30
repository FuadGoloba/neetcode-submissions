class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            remainder = 0 - nums[i]

            while l < r:
                if (nums[l] + nums[r]) < remainder:
                    l += 1
                elif (nums[l] + nums[r]) > remainder:
                    r -= 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1

                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return result
