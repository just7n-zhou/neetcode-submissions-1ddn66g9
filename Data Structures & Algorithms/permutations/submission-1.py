class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [] 

        def backtrack(used, comb):
            if len(comb) == len(nums):
                res.append(comb.copy())
                return 
            
            for i in range(len(nums)):
                if used[i]: continue
                used[i] = True 
                comb.append(nums[i])
                backtrack(used, comb)
                used[i] = False 
                comb.pop()
            
        backtrack([False]*len(nums), [])
        return res 