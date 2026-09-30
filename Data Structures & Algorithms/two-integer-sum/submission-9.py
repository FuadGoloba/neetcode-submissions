class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # SLiding Window
        ordered_nums = []
        for i, num in enumerate(nums):
            ordered_nums.append([num, i])
        
        ordered_nums.sort()
        i, j = 0, len(nums) - 1
        
        while i != j:
            if ordered_nums[i][0] + ordered_nums[j][0] > target:
                j -= 1
            elif ordered_nums[i][0] + ordered_nums[j][0] < target:
                i += 1
            else:
                return [min(ordered_nums[i][1], ordered_nums[j][1]), max(ordered_nums[i][1], ordered_nums[j][1])]

        