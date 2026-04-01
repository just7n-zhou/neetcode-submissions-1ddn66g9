class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p,s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)
        
        fleets = 1 
        prevTime = (target - pairs[0][0]) / pairs[0][1]
        for p,s in pairs[1:]:
            curTime = (target - p) / s 
            if curTime > prevTime:
                fleets += 1 
                prevTime = curTime 
        
        return fleets 