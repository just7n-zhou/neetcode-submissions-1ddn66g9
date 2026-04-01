class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = prefixSum = 0 
        prefixMap = {0 : 1}

        for num in nums:
            prefixSum += num 
            diff = prefixSum - k 
            if diff in prefixMap:
                res += prefixMap[diff]
            prefixMap[prefixSum] = 1 + prefixMap.get(prefixSum,0)
        
        return res 