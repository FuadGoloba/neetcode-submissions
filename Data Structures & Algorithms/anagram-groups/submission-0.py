class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        output = []
        for item in strs:
            sorted_item = ''.join(sorted(item))
            if sorted_item not in anagram_dict:
                anagram_dict[sorted_item] = [item]
            else:
                anagram_dict[sorted_item].append(item)
        
        for k, v in anagram_dict.items():
            output.append(v)
        return output
