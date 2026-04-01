class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            curSum = nums[left] + nums[right]
            if curSum < target:
                left += 1
            elif curSum > target:
                right -= 1
            else:
                return [left + 1, right + 1]
        return []
