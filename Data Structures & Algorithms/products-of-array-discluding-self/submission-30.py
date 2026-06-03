class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n # one initial res with 0 
    
        prefix = 1 # prefix starts with 1 
        for i in range(n): # iterate num forward
            res[i] = prefix # res at each index is equal to current prefix product 
            prefix *= nums[i] # update prefix product to the product of current prefix and current num 
        
        suffix = 1 # suffix also starts with 1 
        for j in range(n - 1, -1, -1): # iterate num backward
            res[j] *= suffix # res at each index is the product of prefix and suffix 
            suffix *= nums[j] # udpate suffix product to the product of current suffix and current num 
        
        return res 