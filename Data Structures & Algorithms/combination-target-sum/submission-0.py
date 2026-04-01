class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(startIndx, subNums, curSum):
            if curSum == target:
                res.append(subNums.copy())
                return 
            
            for i in range(startIndx, len(nums)):
                if curSum + nums[i] > target:
                    return 
                subNums.append(nums[i])
                backtrack(i, subNums, curSum + nums[i])
                subNums.pop()
        
        backtrack(0, [], 0)
        return res