class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums) 
        # divide k by n in case k > n 
        k %= n 

        while k:
            # keep the last element
            temp = nums[n - 1]
            # shift every element to the right 
            for i in range(n - 1, 0, -1):
                nums[i] = nums[i - 1]
            # set the first element euqal to the last element kept
            nums[0] = temp 
            # minus one rotation 
            k -= 1 