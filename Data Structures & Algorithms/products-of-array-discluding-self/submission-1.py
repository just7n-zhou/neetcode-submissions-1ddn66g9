class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1 
        zeroCount = 0 
        for num in nums:
            if num == 0:
                zeroCount += 1 
            else:
                prod *= num 
        
        res = []
        if zeroCount > 1:
            res = [0]*len(nums)
            return res
        elif zeroCount == 1:
            for num in nums:
                if num == 0:
                    res.append(prod)
                else:
                    res.append(0)
            return res 
        else:
            for num in nums:
                res.append(prod // num)
            return res