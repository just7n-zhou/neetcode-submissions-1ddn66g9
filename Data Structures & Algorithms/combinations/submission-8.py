class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(startNum, comb):
            if len(comb) == k:
                res.append(comb.copy())
                return 

            for i in range(startNum, n + 1):
                comb.append(i)
                backtrack(i + 1, comb)
                comb.pop()
        
        backtrack(1, [])
        return res 