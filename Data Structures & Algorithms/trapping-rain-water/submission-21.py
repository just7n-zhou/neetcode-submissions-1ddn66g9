class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        leftMax = [0] * n 
        leftMax[0] = height[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])
        
        rightMax = [0] * n 
        rightMax[n - 1] = height[n - 1]
        for j in range(n - 2, -1, -1):
            rightMax[j] = max(rightMax[j + 1], height[j])
        
        res = 0
        for k in range(n):
            res += min(rightMax[k], leftMax[k]) - height[k]
        
        return res 