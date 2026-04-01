class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        minVal, maxVal = min(nums), max(nums)

        for val in nums:
            count[val] += 1
        
        index = 0
        for i in range(minVal, maxVal + 1):
            while count[i] > 0:
                nums[index] = i 
                index += 1
                count[i] -= 1
        
        return nums 