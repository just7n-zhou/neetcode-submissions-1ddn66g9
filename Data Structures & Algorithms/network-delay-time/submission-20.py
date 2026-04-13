class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n + 1)]
        for u,v, time in times:
            adj[u].append((v, time))
        
        minTime = [float('inf')] * (n + 1)
        minTime[k] = 0 

        pq = [(0, k)]
        visited = [False] * (n + 1)
        count = 0
        while pq:
            cur_time, u = heapq.heappop(pq)
            if visited[u]:
                continue 
            visited[u] = True 
            count += 1

            if count == n:
                break 
            
            for v, weight in adj[u]:
                if not visited[v] and cur_time + weight < minTime[v]:
                    minTime[v] = cur_time + weight 
                    heapq.heappush(pq, (minTime[v],v))
        
        if count != n:
            return -1 
        return max(minTime[1:])
            

