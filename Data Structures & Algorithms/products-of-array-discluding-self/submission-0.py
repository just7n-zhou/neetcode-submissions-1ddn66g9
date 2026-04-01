class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arrayProd = 1
        zeroCount = 0
        for num in nums:
            if num != 0:
                arrayProd *= num
            else:
                zeroCount += 1 

        if zeroCount > 1:
            result = [0]*len(nums)
        elif zeroCount == 1:
            result = []
            for num in nums:
                if num!= 0:
                    result.append(0)
                else:
                    result.append(arrayProd)
        else:
            result = []
            for num in nums:
                result.append(arrayProd // num)
        return result
