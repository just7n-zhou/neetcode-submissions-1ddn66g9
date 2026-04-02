class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums) 
        k = k % n 

        # move last element to front for k times 
        while k:
            # keep the last element 
            temp = nums[n - 1]
            # shift every element to the right once 
            for i in range(n - 1, 0, -1):
                nums[i] = nums[i - 1]
            # set the first element to last element 
            nums[0] = temp 
            k -= 1