class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(startIndx, comb, curSum):
            if curSum == target:
                res.append(comb.copy())
                return 
            
            for i in range(startIndx, len(nums)):
                if curSum + nums[i] > target:
                    return
                curSum += nums[i]
                comb.append(nums[i])
                backtrack(i, comb, curSum)
                curSum -= nums[i]
                comb.pop()
        
        backtrack(0, [], 0)
        return res 