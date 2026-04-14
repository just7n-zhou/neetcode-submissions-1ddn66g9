class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        stack = []
        maxArea = 0 

        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                height = heights[stack.pop()]

                width = i - stack[-1] -1 
                area = height * width 
                maxArea = max(maxArea, area)
            
            stack.append(i)
        
        return maxArea 