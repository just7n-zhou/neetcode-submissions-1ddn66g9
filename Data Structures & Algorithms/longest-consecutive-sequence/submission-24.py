class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0 

        for num in nums:
            # if num -1 not in the set 
            # meaning current num is start of a new sequence
            if num - 1 not in numSet:
                length = 1 
                while num + length in numSet:
                    length += 1 
                
                longest = max(longest, length)
        
        return longest 