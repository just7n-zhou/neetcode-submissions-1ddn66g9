class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        # Track the maximum height seen from left and right
        leftMax, rightMax = height[l], height[r]
        res = 0
        
        # Process until pointers meet
        while l < r:
            # Process the side with smaller current max
            if leftMax < rightMax:
                # Move left pointer inward
                l += 1
                # Update left max to include current bar
                leftMax = max(leftMax, height[l])
                # Add water trapped at current position
                # Water = min(leftMax, rightMax) - height[l]
                # Since leftMax < rightMax, min = leftMax
                res += leftMax - height[l]
            else:
                # Move right pointer inward
                r -= 1
                # Update right max to include current bar
                rightMax = max(rightMax, height[r])
                # Add water trapped at current position
                # Water = min(leftMax, rightMax) - height[r]
                # Since rightMax <= leftMax, min = rightMax
                res += rightMax - height[r]
                
        return res