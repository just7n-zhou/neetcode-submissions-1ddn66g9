class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Make a default dictionary of list 
        myDict = defaultdict(list)
        for word in strs:
            # sorted() return a list of character
            # "".join() to convert to str 
            sortedWord = "".join(sorted(word))

            # put each unique anagram to myDict as key 
            # Append word that is that anagram into the list of that key
            myDict[sortedWord].append(word)

            # Return the value of each unique anagram list 
        return list(myDict.values())