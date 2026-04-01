class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(startIndx, comb):
            if startIndx == len(s):
                res.append(comb.copy())
                return 
            
            for i in range(startIndx, len(s)):
                if s[startIndx: i + 1] == s[startIndx: i + 1][::-1]:
                    comb.append(s[startIndx:i + 1])
                    backtrack(i + 1, comb)
                    comb.pop()
            
        backtrack(0,[])
        return res 