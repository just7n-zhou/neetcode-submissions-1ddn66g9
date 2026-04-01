class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        for i, num in enumerate(nums):
            complement = target - num 
            if complement in mydict:
                return [mydict[complement], i]
            mydict[num] = i 
        
        return []