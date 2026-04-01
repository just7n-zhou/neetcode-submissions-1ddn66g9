class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # add 0 on both sides
        # left zero: ensure stack never empty 
        # right zero: ensure to pop all heights from stack for processing 
        heights = [0] + heights + [0] 
        stack = [] # increasing stack, store index
        maxArea = 0 

        for i, h in enumerate(heights):
            # keeping poping from stack if current is shorter than top of stack 
            while stack and h < heights[stack[-1]]:
                # pop stack top 
                height = heights[stack.pop()]
                # right bondary of poped height is current height 
                # left bondary is the new stack top (left of popped height)
                width = i - stack[-1] - 1 
                # calculate the area based on wid and height
                area = height * width 
                maxArea = max(maxArea, area)
            # if current is higher, add to stack
            stack.append(i)
        
        return maxArea