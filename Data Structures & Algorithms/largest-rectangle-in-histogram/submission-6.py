class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        maxArea = 0 
        stack = [] #monotonic stack (store index)

        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                curHeight = heights[stack.pop()]

                leftBond = stack[-1]
                rightBond = i 
                
                width = rightBond - leftBond - 1
                curArea = width * curHeight
                maxArea = max(maxArea, curArea)
            
            stack.append(i)
        
        return maxArea 