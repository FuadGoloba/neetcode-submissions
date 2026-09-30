class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        # 1. sort array in order and to exclude duplicate processing
        nums.sort()

        # 2. Traverse each number in array as a possible first candidate and process against rest of array
        # 2.1 Skip already processed canndidate 
        for first in range(len(nums)):
            if first > 0 and nums[first - 1] == nums[first]:
                continue

            second, third = first + 1, len(nums) - 1
            target = 0 - nums[first]
            # 2.2 While processing rest of array, we use 2 pointers technique at each end of array to determine triplet permissibility
            while second < third:
                if nums[second] + nums[third] == target:
                    result.append([nums[first], nums[second], nums[third]])
                    second += 1

                    while nums[second] == nums[second - 1] and second < third:
                        second += 1
                        
                elif nums[second] + nums[third] < target:
                    second += 1
                else:
                    third -= 1

        return result
