class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        maxVal, minVal = max(nums), min(nums)
        for val in nums:
            count[val] += 1
        
        index = 0 
        for val in range(minVal, maxVal + 1):
            while count[val] > 0:
                nums[index] = val 
                count[val] -= 1
                index += 1
        
        return nums 