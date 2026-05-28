class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums) 
        res = [0] * n * 2
        for i in range(len(nums)):
            res[i] = res[i + n] = nums[i]
        
        return res 