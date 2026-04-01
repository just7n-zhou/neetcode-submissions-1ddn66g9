class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Bellman-Ford solution
        minDist = [float('inf')] * (n + 1)
        minDist[k] = 0

        # relax all edges n-1 times
        for _ in range(1, n):
            updated = False 
            for u, v, weight in times:
                if minDist[u] != float('inf') and minDist[u] + weight < minDist[v]:
                    minDist[v] = minDist[u] + weight
                    updated = True 
            
            if not updated:
                break 
        
        maxDist = max(minDist[1:])
        return maxDist if maxDist != float('inf') else -1 
 