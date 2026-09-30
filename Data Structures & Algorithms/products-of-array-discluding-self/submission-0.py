class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        product = [0] * len(nums)

        prefix = 1
        for idx in range(len(nums)):
            product[idx] = prefix
            prefix *= nums[idx] 

        suffix = 1
        for idx in range(len(nums) -1, -1, -1):
            product[idx] *= suffix
            suffix *= nums[idx]

        return product