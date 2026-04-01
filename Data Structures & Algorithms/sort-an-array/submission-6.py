class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # A list of 1 or 0 is already sorted
        if len(nums) <= 1:
            return nums 
        
        mid = len(nums) // 2 
        left_half = self.sortArray(nums[:mid])
        right_half = self.sortArray(nums[mid:])

        return self.merge(left_half, right_half)

    def merge(self, leftSide, rightSide):
        res = []
        i = j = 0 

        while i < len(leftSide) and j < len(rightSide):
            if leftSide[i] < rightSide[j]:
                res.append(leftSide[i])
                i += 1
            else:
                res.append(rightSide[j])
                j += 1
        
        res.extend(leftSide[i:])
        res.extend(rightSide[j:])

        return res 