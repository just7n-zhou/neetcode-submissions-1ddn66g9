class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # heap-optimized Dijkstra 
        # 1. Build the Adjacency List: {from: [(to, weight), ...]}
        adj = collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
            
        # 2. Track the minimum time to reach each node
        # n + 1 because nodes are labeled 1 to n
        min_times = [float('inf')] * (n + 1)
        min_times[k] = 0
        
        # 3. Priority Queue: (time_spent, current_node)
        pq = [(0, k)]
        
        # To keep track of finalized nodes
        visited = [False] * (n + 1)
        count = 0 # How many nodes have received the signal
        
        while pq:
            time, u = heapq.heappop(pq)
            
            # Standard Dijkstra: if we already found a shorter path to u, skip
            if visited[u]:
                continue
            
            visited[u] = True
            count += 1
            
            # Optimization: If we've reached all n nodes, we can stop early
            if count == n:
                break
            
            # Explore neighbors
            for v, weight in adj[u]:
                if not visited[v] and time + weight < min_times[v]:
                    min_times[v] = time + weight
                    heapq.heappush(pq, (min_times[v], v))
                    
        # 4. Result logic
        # We only care about nodes 1 to n. 
        # If we couldn't reach all n nodes, return -1.
        if count < n:
            return -1
            
        # The answer is the time it took to reach the furthest node
        # We ignore index 0 because nodes are 1-indexed
        max_time = 0
        for i in range(1, n + 1):
            max_time = max(max_time, min_times[i])
            
        return max_time
