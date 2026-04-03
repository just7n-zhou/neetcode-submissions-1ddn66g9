class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Normal Bellman-Ford 
        # 1. Build adjacency list for efficient neighbor lookup
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
            
        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        
        # 2. Queue stores nodes that were recently updated
        queue = deque([k])
        
        # in_queue avoids adding a node that's already waiting to be processed
        in_queue = [False] * (n + 1)
        in_queue[k] = True
        
        while queue:
            u = queue.popleft()
            in_queue[u] = False
            
            for v, w in adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    
                    if not in_queue[v]:
                        queue.append(v)
                        in_queue[v] = True
        
        # 3. Final result logic
        max_dist = max(dist[1:])
        return max_dist if max_dist != float('inf') else -1
            
        # The answer is the time it took to reach the furthest node
        # We ignore index 0 because nodes are 1-indexed
        max_time = 0
        for i in range(1, n + 1):
            max_time = max(max_time, min_times[i])
            
        return max_time
