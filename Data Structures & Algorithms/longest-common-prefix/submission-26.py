class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        reference = strs[0]

        for i in range(1, len(strs)):
            j = 0 
            while j < min(len(reference), len(strs[i])):
                if reference[j] != strs[i][j]:
                    break 
                j += 1

            reference = reference[:j]
        
        return reference