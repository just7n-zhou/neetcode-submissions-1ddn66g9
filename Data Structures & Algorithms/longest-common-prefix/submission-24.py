class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        reference  = strs[0]

        for i in range(len(reference)):
            for s in strs:
                if i == len(s) or s[i] != reference[i]:
                    return s[:i]
        
        return reference 