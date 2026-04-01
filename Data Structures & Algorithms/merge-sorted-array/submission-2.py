class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        midx, nidx = m - 1, n - 1 
        right = m + n - 1

        while nidx >= 0:
            if nums1[midx] > nums2[nidx] and midx >=0:
                nums1[right] = nums1[midx]
                midx -= 1
            else:
                nums1[right] = nums2[nidx]
                nidx -= 1
            right -= 1
        