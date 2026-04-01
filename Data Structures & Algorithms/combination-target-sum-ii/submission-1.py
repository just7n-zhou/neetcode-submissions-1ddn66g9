class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(startIndx, curSum, comb):
            if curSum == target:
                res.append(comb.copy())
                return 

            for i in range(startIndx, len(candidates)):
                if i > startIndx and candidates[i - 1] == candidates[i]:
                    continue
                if curSum + candidates[i] > target:
                    break 

                curSum += candidates[i]
                comb.append(candidates[i])
                backtrack(i + 1, curSum, comb)
                curSum -= candidates[i]
                comb.pop()
            
        backtrack(0, 0, [])
        return res 