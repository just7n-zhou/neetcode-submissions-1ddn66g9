class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]
                if diff < 0:
                    stack.pop() # positive asteroid on top of stack is destryoed 
                elif diff > 0:
                    a = 0 # the negative asteroid is destroyed
                else:
                    # both are destroyed
                    a = 0 
                    stack.pop()
            # if incoming asteroid still survived, add to stack 
            if a:
                stack.append(a)
        
        return stack 