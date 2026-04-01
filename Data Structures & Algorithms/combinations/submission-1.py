class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(startIndex, combin):
            if len(combin) == k:
                res.append(combin.copy())
                return 
            
            for i in range(startIndex, n + 1):
                combin.append(i)
                backtrack(i + 1, combin)
                combin.pop()
        
        backtrack(1, [])
        return res 