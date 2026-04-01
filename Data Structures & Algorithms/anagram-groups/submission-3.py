class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = defaultdict(list)
        for s in strs:
            sortedS = "".join(sorted(s))
            anagramMap[sortedS].append(s)
        
        res = []
        for anagramList in anagramMap.values():
            res.append(anagramList)
        return res