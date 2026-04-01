class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = curSum = 0 
        prefixSum = { 0 : 1 } 
        
        for num in nums:
            curSum += num 
            diff = curSum - k 
            if diff in prefixSum:
                res += prefixSum[diff]
            if curSum in prefixSum:
                prefixSum[curSum] += 1
            else:
                prefixSum[curSum] = 1

        return res