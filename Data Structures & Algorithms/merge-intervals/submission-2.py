class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res = []

        for interval in intervals:
            # it res is empty or current's first num is greater than second num in the top interval in res
            # meaning no overlap, append current interval to res
            if not res or interval[0] > res[-1][1]:
                res.append(interval)
            # other wise update the second num in the top interval in res 
            else:
                res[-1][1] = max(interval[1], res[-1][1])
        
        return res 