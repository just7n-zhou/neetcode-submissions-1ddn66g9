class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for indx, curT in enumerate(temperatures):
            while stack and curT > stack[-1][0]:
                stackT, stackIndx = stack.pop()
                res[stackIndx] = indx - stackIndx
            stack.append((curT, indx))
        
        return res 