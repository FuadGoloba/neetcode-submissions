class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        result = []

        for w in strs:
            sorted_w = str(sorted(w))
            anagrams[sorted_w] = anagrams.get(sorted_w, []) + [w]

        for value in anagrams.values():
            result.append(value)

        return result