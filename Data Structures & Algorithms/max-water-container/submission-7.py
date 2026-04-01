class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0 
        left, right = 0, len(heights) - 1

        while left < right:
            water = min(heights[left], heights[right]) * (right - left)
            maxWater = max(maxWater, water)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return maxWater 