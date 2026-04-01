class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}
        for i in range(len(nums)):
            complement = target - nums[i]             
            if complement in myDict:
                return [myDict[complement], i]
            else:
                myDict[nums[i]] = i
        return [] 