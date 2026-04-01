class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = maxCount = 0 
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
            if count[num] > maxCount:
                res = num 
                maxCount = count[num]
        
        return res 