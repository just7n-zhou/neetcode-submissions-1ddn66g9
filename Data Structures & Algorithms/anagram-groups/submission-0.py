class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = defaultdict(list)

        for word in strs:
            sortedWord = "".join(sorted(word))
            myDict[sortedWord].append(word)
        return list(myDict.values())