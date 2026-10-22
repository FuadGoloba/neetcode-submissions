class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyMap = {} # Hashmap to map items to their frequency
        freq_list = [[] for i in range(len(nums) + 1)] # List to store a list for every index of the array
        
        # Traverse the array mapping each item to its frequency
        for item in nums:
            frequencyMap[item] = frequencyMap.get(item, 0) + 1
        
        # Traverse the frequency map and for each index/count in the frequency list(index <=> count), append the item to the list (So you have a list of list of hashmap's keys where the index is the count/frequency of the key)
        for item, count in frequencyMap.items():
            freq_list[count].append(item)
        
        result = [] # Result to store top K frequent elements
        # Traverse the list starting from the end, each item to the 1th index
        for index in range(len(freq_list) - 1, 0, -1): 
            for item in freq_list[index]: # Traverse the inner list of each index (i.e each index here is the count/frequency) and append the numbers in the list to the final result list
                result.append(item)
                if len(result) == k:
                    return result
