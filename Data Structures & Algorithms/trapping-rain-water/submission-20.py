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
                # Move left pointer to check current index 
                l += 1
                # check if current height is greater than leftMax 
                # if yes, update leftMax. Do it for every l index 
                leftMax = max(leftMax, height[l])
                
                res += leftMax - height[l]
            else:
                # Move right pointer to check current index 
                r -= 1
                # same for right pointer 
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        
        return res 