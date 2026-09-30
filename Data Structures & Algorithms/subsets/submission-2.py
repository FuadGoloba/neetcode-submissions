class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
    
        smaller_subsets = self.subsets(nums[1:])
        all_subsets = []
        
        for subset in smaller_subsets:
            all_subsets.append(subset)
            all_subsets.append([nums[0]] + subset)
            
        return all_subsets