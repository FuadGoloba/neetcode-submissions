class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        result = []

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        sorted_freq = sorted(freq.items(), key=lambda kv: kv[1], reverse=True)

        for key, v in sorted_freq:
            if len(result) != k:
                result.append(key)

        return result