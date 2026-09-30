class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        output = []
        frequency_list = [ [] for i in range(len(nums) + 1) ]

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        for key, val in frequency.items():
            frequency_list[val].append(key)

        for  i in range(len(frequency_list) -1, 0, -1):
            if frequency_list[i] != []:
                for num in frequency_list[i]:
                    if len(output) == k:
                        break
                    output.append(num)
                
        return output