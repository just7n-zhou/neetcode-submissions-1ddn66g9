class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(startIndx, comb):
            res.append(comb.copy())
            if startIndx >= len(nums):
                return 
            for i in range(startIndx, len(nums)):
                comb.append(nums[i])
                backtrack(i + 1, comb)
                comb.pop()
        
        backtrack(0, [])
        return res 
