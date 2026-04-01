class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1 
        zeroCount = 0 
        for n in nums:
            if n == 0:
                zeroCount += 1
            else:
                prod *= n
        
        if zeroCount > 1:
            return [0] * len(nums)
        if zeroCount == 1:
            res = []
            for n in nums:
                if n == 0:
                    res.append(prod)
                else:
                    res.append(0)
        if zeroCount == 0:
            res = []
            for n in nums:
                res.append(prod // n)
        
        return res