class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = defaultdict(list)
        for s in strs:
            sortedS = "".join(sorted(s))
            anagramMap[sortedS].append(s)
        return list(anagramMap.values())

