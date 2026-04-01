class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # initial version of solution division 
        prod = 1 
        zeroCount = 0 
        for num in nums:
            if num == 0:
                zeroCount += 1
            else:
                prod *= num 
        
        if zeroCount > 1:
            return [0]*len(nums)
        if zeroCount == 1:
            res = []
            for num in nums:
                if num!= 0:
                    res.append(0)
                else:
                    res.append(prod)
            return res
        if zeroCount == 0:
            res = []
            for num in nums:
                res.append(prod // num)
            return res

            
