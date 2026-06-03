class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n # products of all numbers before each index 
        suffix  = [0] * n # products of all numbers after each index 
        res = [0] * n # products of prefix and suffix at each index

        prefix[0] = suffix[n-1] = 1 # begin of each arr is always 1 

        # populate prefix and suffix 
        for i in range(1, n):
            prefix[i] = nums[i - 1] * prefix[i - 1]
        for i in range(n - 2, -1, -1):
            suffix[i] = nums[i + 1] * suffix[i + 1]
        # products of prefix and suffix at each index 
        for i in range(n):
            res[i] = prefix[i] * suffix[i]
        
        return res 