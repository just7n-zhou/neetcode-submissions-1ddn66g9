class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0 
        
        leftMax = [0] * n 
        rightMax = [0] * n

        # prefix max to the left of each i 
        leftMax[0] = height[0]
        for i in range(1, n):
            # leftMax[i-1] already contain max value from index 0 to i - 1
            leftMax[i] = max(leftMax[i - 1], height[i])

        rightMax[n - 1] = height[n-1]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])
        
        
        res = 0 
        for i in range(n):
            res += min(leftMax[i], rightMax[i]) - height[i]
        
        return res 