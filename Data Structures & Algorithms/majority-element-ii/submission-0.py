class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        target = n // 3
        res = set()
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
            if count[num] > target:
                res.add(num)
        
        return list(res)