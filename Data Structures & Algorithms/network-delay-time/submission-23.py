class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n + 1)]
        for u, v, time in times:
            adj[u].append((v, time))
        
        minTimes = [float('inf')] * (n + 1)
        minTimes[k] = 0 

        pq = [(0, k)]
        visited = [False] * (n + 1)
        count = 0

        while pq:
            curTime, u = heapq.heappop(pq)
            if visited[u]:
                continue 
            visited[u] = True 

            count += 1
            if count == n:
                break 
            
            for v, time in adj[u]:
                if curTime + time < minTimes[v]:
                    minTimes[v] = curTime + time 
                    heapq.heappush(pq, (minTimes[v], v))
        
        if count != n:
            return -1 
        return max(minTimes[1:]) if max(minTimes[1:]) != float('inf') else -1 