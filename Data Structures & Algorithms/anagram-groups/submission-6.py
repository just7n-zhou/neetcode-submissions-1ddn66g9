class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            anagram_map[sorted_s].append(s) 
        
        res = []
        for anagrams in anagram_map.values():
            res.append(anagrams)
        
        return res