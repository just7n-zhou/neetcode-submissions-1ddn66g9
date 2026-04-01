class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Base Case: A list of 0 or 1 elements is already sorted
        if len(nums) <= 1:
            return nums
        
        # 1. Divide
        mid = len(nums) // 2
        left_half = self.sortArray(nums[:mid])
        right_half = self.sortArray(nums[mid:])
        
        # 2. Conquer & Combine
        return self.merge(left_half, right_half)

    def merge(self, left, right):
        res = []
        i = j = 0
        
        # Compare elements from both halves and add the smaller one to 'res'
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        
        # If there are remaining elements in left or right, add them
        res.extend(left[i:])
        res.extend(right[j:])
        
        return res