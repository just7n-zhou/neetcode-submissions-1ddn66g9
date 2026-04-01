class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        refer = strs[0]

        for i in range(len(refer)):
            for s in strs[1:]:
                if i == len(s) or refer[i] != s[i]:
                    return s[:i]
        
        return refer 