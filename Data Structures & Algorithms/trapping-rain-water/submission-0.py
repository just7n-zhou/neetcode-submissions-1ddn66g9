class Solution:
    def trap(self, height: List[int]) -> int:
        # brutal force 
        # for each element in array, check its adjacent height 
        # calculate max number of water it can trap:
        # Min of max height of bars on both side minus its own height
        ans = 0 
        for i in range(1, len(height) - 1):
            leftMax = 0
            rightMax = 0
            # search for max bar side on left of height[i]
            for j in range(i, -1, -1):
                leftMax = max(leftMax, height[j])
            # search for max bar side on left of height[i]
            for j in range(i, len(height)):
                rightMax = max(rightMax, height[j])
                
            ans += min(leftMax, rightMax) - height[i]
        return ans