class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))
        
        minTime = [float('inf')] * (n + 1)
        minTime[k] = 0
        visited = [False] * (n + 1)

        pq = [(0, k)]
        count = 0
        while pq:
            curT, u = heapq.heappop(pq)
            if visited[u]:
                continue 
            
            visited[u] = True 
            count += 1

            if count == n:
                break 
            
            for v, t in adj[u]:
                if not visited[v] and t + curT < minTime[v]:
                    minTime[v] = t + curT
                    heapq.heappush(pq, (minTime[v], v))
        
        if count < n:
            return -1 
        
        maxTime = 0 
        for i in range(1, len(minTime)):
            maxTime = max(maxTime, minTime[i])
        
        return maxTime 