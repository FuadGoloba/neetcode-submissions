class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        longest = 0

        for n in numSet:
            # start of a new sequence
            if (n - 1) not in numSet:
                # calculate the next ranges we find in the numset
                curr_seq = 1
                nxt = n + 1
                while nxt in numSet:
                    curr_seq += 1
                    nxt += 1
                longest = max(longest, curr_seq)
        return longest




