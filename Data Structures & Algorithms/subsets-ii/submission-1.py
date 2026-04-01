class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(startIndx, comb):
            res.append(comb.copy())
            for i in range(startIndx, len(nums)):
                if i > startIndx and nums[i] == nums[i - 1]:
                    continue 
                comb.append(nums[i])
                backtrack(i + 1, comb)
                comb.pop()
        
        backtrack(0, [])
        return res 