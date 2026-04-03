class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Queue-Optimized Bellman-Ford solution (Shortest Path Faster Algorithm)
        # 1. Build adjacency list for efficient neighbor lookup
        adj = defaultdict(list)
        for u, v, weight in times:
            adj[u].append((v, weight))
        
        minDist = [float('inf')] * (n + 1)
        minDist[k] = 0 

        # 2. Queue stores nodes that were recently updated
        queue = deque([k])
        # visited[] avoids duplicate processing 
        visited = [False] * (n + 1)
        visited[k] = True

        # 3. iterate through queue like BFS 
        while queue:
            u = queue.popleft()
            # set popped node to False allow u to be re-added to queue later
            # if a shorter path is found 
            visited[u] = False  
            for v, weight in adj[u]:
                if minDist[u] + weight < minDist[v]:
                    minDist[v] = minDist[u] + weight
                    # if a destination node is already visited, meaning it's already in queue
                    # then don't add it to queue again
                    if visited[v] == False:
                        queue.append(v)
                        visited[v] = True
        
        maxDist = max(minDist[1:])
        return maxDist if maxDist != float('inf') else -1 