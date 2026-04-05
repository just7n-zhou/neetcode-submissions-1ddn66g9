class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use set for const loop up and keep track of unique char 
        charSet = set()
        # left pointer to shrink window
        l = res = 0 
        # right pointer to expand window
        for r in range(len(s)):
            # if encounter a duplicate with r pointer
            while s[r] in charSet:
                # keep removing the left pointer(shrink window)
                # until no duplicate
                charSet.remove(s[l])
                l += 1
            # then add char at right pointer to set
            charSet.add(s[r])
            # compare current set len with res and update res 
            res = max(res, len(charSet))
        
        return res 