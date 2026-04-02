class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        # Only binary search the shorter array 
        # Set A to always be the shorter array 
        if len(B) < len(A):
            A, B = B, A
        
        l, r = 0, len(A) - 1 # indices of A
        while True:
            # i is index of last num in left part of A, number of element is i + 1 
            # j is index of last num in left part of B, number of element is j + 1
            # num from left of A and left of B should sum up to half 
            # So i + 1 + j + 1 = half => j = half - i - 2
            i = (l + r) // 2
            j = half - i - 2

            # i there is one side with no elements, replace it with infinity 
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")
            
            # Core idea: median of sorted array is where left of it is always smaller than the right of it 
            # right side of (max of) left of A should be smaller than the left side (min of) of right of B 
            # right side of (max of) left of B should be smaller than the left side of (min of) right of A 
            if Aleft <= Bright and Bleft <= Aright:
                # if combined array has odd length
                if total % 2 == 1:
                    return min(Aright, Bright)
                # if combined array has even length
                else:
                    #      max of left side     min of right side
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            # if the core condition is not met, 
            # if right side of left of A is bigger than left of right of B 
            # meaning there are too many element at A, move right pointer to left of i 
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1