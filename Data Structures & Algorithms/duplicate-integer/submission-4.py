class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mySet = set(nums)
        if len(mySet) != len(nums):
            return True 
        else:
            return False 