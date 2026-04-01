class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0 

        for n in nums:
            # check if it's start of a sequence
            if (n - 1) not in numSet:
                sequenceLength = 1 
                while (n + sequenceLength) in numSet:
                    sequenceLength += 1
                longest = max(sequenceLength, longest)
        
        return longest 