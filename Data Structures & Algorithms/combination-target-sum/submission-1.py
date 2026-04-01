class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(curSum, startIndx, comb):
            if curSum > target:
                return 
            if curSum == target:
                res.append(comb.copy())
                return 
            
            for i in range(startIndx, len(nums)):
                curSum += nums[i]
                comb.append(nums[i])
                backtrack(curSum, i, comb)
                curSum -= nums[i]
                comb.pop()
        
        backtrack(0, 0, [])
        return res 