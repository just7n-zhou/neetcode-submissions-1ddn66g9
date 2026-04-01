class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Make a default dictionary of list 
        myDict = defaultdict(list)
        for word in strs:
            # sorted() return a list of character
            # "".join() to convert to str 
            sortedWord = "".join(sorted(word))
            myDict[sortedWord].append(word)
        return list(myDict.values())