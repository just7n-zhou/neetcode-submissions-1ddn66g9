class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixMap = {0 : 1}
        prefixSum = 0 
        res = 0 

        res = 0
        for num in nums:
            prefixSum += num 
            if prefixSum - k in prefixMap:
                res += prefixMap[prefixSum -k]
            prefixMap[prefixSum] = prefixMap.get(prefixSum, 0) + 1
        
        return res 