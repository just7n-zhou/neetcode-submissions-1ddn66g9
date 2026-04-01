class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[right]: # if true, min is in left half
                right = mid
            else: # otherwise, min is in right half
                left = mid + 1
        
        # when loop ends, left points to smallest
        return nums[left]