class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_list = [[] for i in range(len(nums) + 1)]
        freq_map = {}
        result = []

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        for num, freq in freq_map.items():
            freq_list[freq].append(num)

        for i in range(len(freq_list) - 1, 0, -1):
            for num in freq_list[i]:
                if len(result) < k:
                    result.append(num)

        return result


        

