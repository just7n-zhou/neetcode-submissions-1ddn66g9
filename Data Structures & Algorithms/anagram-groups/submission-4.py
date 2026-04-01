class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = defaultdict(list)
        for s in strs:
            sortedS = "".join(sorted(s))
            myDict[sortedS].append(s)

        res = []
        for wordList in myDict.values():
            res.append(wordList)
        return res