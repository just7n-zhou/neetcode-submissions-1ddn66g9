class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)

        res = maxCount = 0 

        for num in nums:
            count[num] += 1
        
        for num, cnt in count.items():
            if cnt > maxCount:
                maxCount = cnt 
                res = num 
        
        return res 
