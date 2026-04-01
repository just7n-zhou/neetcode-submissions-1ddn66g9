class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        size = min(len(word1), len(word2))
        res = ""
        for i in range(size):
            res += (word1[i])
            res += (word2[i])
        
        if len(word1) > len(word2):
            res += (word1[size:])
        else:
            res += (word2[size:])
        
        return res 