class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(used, comb):
            if len(comb) == len(nums):
                res.append(comb.copy())
                return 
            
            for i in range(len(nums)):
                if (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]) or used[i]:
                    continue 
                used[i] = True 
                comb.append(nums[i])
                backtrack(used, comb)
                used[i] = False 
                comb.pop()
        
        backtrack([False]*len(nums), [])
        return res 
