class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        
        def upper_bound(nums, target):
            ''' Returns the index of the last occurrence of target'''
            l, r = 0, len(nums) - 1
            index = -1
            while l <= r:
                mid = (l + r) // 2
                if target == nums[mid]:
                    index = mid
                    l = mid + 1
                elif target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            return index

        def lower_bound(nums, target):
            '''Returns the index of the first coccurence of target'''
            l, r = 0, len(nums) - 1
            index = 0

            while l <= r:
                mid = (l + r) // 2
                if target == nums[mid]:
                    index = mid
                    r = mid - 1
                elif target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            return index

        first, last = lower_bound(nums, target), upper_bound(nums, target)
        return ((last - first) + 1) > len(nums) / 2