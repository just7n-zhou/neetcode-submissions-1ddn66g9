class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, curT in enumerate(temperatures):
            while stack and curT > stack[-1][0]:
                stackT, stackIndx = stack.pop()
                res[stackIndx] = i - stackIndx
            stack.append((curT, i))
        
        return res 