class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(startIndx, curSum, comb):
            if curSum > target:
                return
            if curSum == target:
                res.append(comb.copy())
                return 
            
            for i in range(startIndx, len(nums)):
                curSum += nums[i]
                comb.append(nums[i])
                backtrack(i, curSum, comb)
                curSum -= nums[i]
                comb.pop()
        
        backtrack(0, 0, [])
        return res 