class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        minVal, maxVal = min(nums), max(nums)
        res = []
        for val in range(minVal, maxVal+1):
            while count[val]:
                res.append(val)
                count[val] -= 1
        
        return res 