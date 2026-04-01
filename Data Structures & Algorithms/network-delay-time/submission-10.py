class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v, time in times:
            adj[u].append((v, time))
        
        minDist = [float('inf')] * (n + 1)
        minDist[k] = 0 

        queue = deque([k])
        visited = [False]*(n+1)
        visited[k] = True 

        while queue:
            u = queue.popleft()

            visited[u] = False 
            for v, time in adj[u]:
                if minDist[u] + time < minDist[v]:
                    minDist[v] = minDist[u] + time 

                    if visited[v] == False:
                        queue.append(v)
                        visited[v] = True 
        
        maxDist = max(minDist[1:])
        return maxDist if maxDist != float('inf') else -1 