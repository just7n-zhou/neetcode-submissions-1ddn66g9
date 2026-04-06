class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxWater = 0 

        while l < r:
            h, w =  min(heights[l], heights[r]), (r - l)
            curWater = h * w 
            maxWater = max(curWater, maxWater)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxWater