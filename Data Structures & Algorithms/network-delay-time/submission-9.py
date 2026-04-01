class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v, time in times:
            adj[u].append((v, time))
        
        minTime = [float('inf')] * (n + 1)
        minTime[k] = 0 

        queue = [(0, k)]
        visited = [False] * (n + 1)
        count = 0

        while queue:
            time, u = heapq.heappop(queue)

            if visited[u]:
                continue 
            
            visited[u] = True 
            count += 1

            if count == n:
                break 
            
            for v, weight in adj[u]:
                if not visited[v] and time + weight < minTime[v]:
                    minTime[v] = time + weight 
                    heapq.heappush(queue, (minTime[v],v))

        if count < n:
            return - 1 
        
        maxTime = 0 
        for i in range(1, len(minTime)):
            maxTime = max(maxTime, minTime[i])
        
        return maxTime 