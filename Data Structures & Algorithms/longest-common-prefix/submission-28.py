class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        refer = strs[0]

        for i in range(1, len(strs)):
            j = 0 
            while j < min(len(refer), len(strs[i])):
                if refer[j] != strs[i][j]:
                    break 
                j += 1
            
            refer = refer[:j]
        
        return refer 
