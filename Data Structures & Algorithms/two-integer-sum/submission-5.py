class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in mydict:
                return [mydict[compliment], i]
            mydict[num] = i 
        
        return []
