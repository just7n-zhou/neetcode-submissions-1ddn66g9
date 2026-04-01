class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # [(temp, index)]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]: # check if cur t is greater than temp at top of stack
                stackT, stackIndx = stack.pop()
                res[stackIndx] = i - stackIndx
            stack.append((t,i))
        
        return res 