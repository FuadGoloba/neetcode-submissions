class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) == 0:
            return [[]]

        curr_perms = self.permute(nums[1:])
        all_permutations = []

        for perm in curr_perms:
            for i in range(len(perm) + 1):
                perm_copy = perm.copy()
                perm_copy.insert(i, nums[0])
                all_permutations.append(perm_copy)
            
        return all_permutations