class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        def backtrack(startIndx, curSum, comb):
            if curSum == target:
                res.append(comb.copy())
                return 
            for i in range(startIndx, len(candidates)):
                if i > startIndx and candidates[i] == candidates[i-1]:
                    continue 
                if curSum + candidates[i] > target:
                    break 
                
                comb.append(candidates[i])
                backtrack(i + 1, curSum + candidates[i], comb)
                comb.pop()
            
        backtrack(0, 0, [])
        return res 