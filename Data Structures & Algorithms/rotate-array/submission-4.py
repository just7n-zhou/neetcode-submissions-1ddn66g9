class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        temp = [0] * len(nums)
        for i in range(n):
            temp[(i + k) % n] = nums[i]
        
        nums[:] = temp