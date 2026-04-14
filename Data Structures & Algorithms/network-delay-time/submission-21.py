class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n + 1)]
        for u, v, weight in times:
            adj[u].append((v, weight))
        
        visited =[False] * (n + 1)
        minTime = [float('inf')] * (n + 1)
        minTime[k] = 0 
        count = 0 

        pq = [(0, k)]

        while pq:
            curTime, u = heapq.heappop(pq)
            
            if visited[u]:
                continue 
            visited[u] = True
            count += 1

            for v, time in adj[u]:
                if curTime + time < minTime[v]:
                    minTime[v] = curTime + time 
                    heapq.heappush(pq, (minTime[v], v))
        
        if count != n:
            return -1 
        return max(minTime[1:]) if max(minTime[1:]) != float('inf') else -1 
        
        
