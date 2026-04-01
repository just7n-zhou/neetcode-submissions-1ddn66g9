class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        stack = []
        maxArea = 0 

        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                curHighest = heights[stack.pop()] 

                leftBond = stack[-1]
                rightBond = i 

                width = rightBond - leftBond - 1
                curArea = width * curHighest 
                maxArea = max(maxArea, curArea)
            
            stack.append(i)

        return maxArea 