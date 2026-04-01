class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        reference = strs[0]

        for i in range(len(reference)):
            for s in strs[1:]:
                if i == len(s) or reference[i] != s[i]:
                    return s[:i]
        
        return reference 