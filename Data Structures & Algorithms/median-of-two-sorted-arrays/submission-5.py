class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the shorter array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1 
        
        m, n = len(nums1), len(nums2)
        l, r = 0, m
        
        while l <= r:
            i = (l + r) // 2  # elements from nums1 in left partition, serve as mid of combined array 
            j = (m + n + 1) // 2 - i  # elements from nums2 in left partition
            
            # 0-indexed, or i - 1 is the right side of left partition
            left1 = nums1[i-1] if i > 0 else float('-inf')
            right1 = nums1[i] if i < m else float('inf')
            left2 = nums2[j-1] if j > 0 else float('-inf')
            right2 = nums2[j] if j < n else float('inf')
            

            # left sides of each array should be smaller than the right side 
            # of its other array 
            if left1 <= right2 and left2 <= right1:
                # if total len is odd, the max of two left partitions is the 
                # right bondary of combined array 
                if (m + n) % 2 == 1:
                    return max(left1, left2)
                # if total len is even, return the mean of middle two elements 
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2
            # if left 1 is bigger, meaning there are more elements in nums1 than it should be 
            # move right pointer to the left of i, which is the mid of combined array 
            elif left1 > right2:
                r = i - 1
            # otherwise move the left pointer to the right of i 
            else:
                l = i + 1
        
        return 0.0  # Should never reach here for valid inputs
