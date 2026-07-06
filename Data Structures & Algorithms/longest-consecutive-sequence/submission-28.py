class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums) # convert to num for constant look up 
        longest = 0 

        for num in nums:
            if num - 1 not in num_set: # meaning current num is start of a new sequence
                length = 1
                while num + length in num_set:
                    length += 1
                longest = max(longest, length)
        
        return longest