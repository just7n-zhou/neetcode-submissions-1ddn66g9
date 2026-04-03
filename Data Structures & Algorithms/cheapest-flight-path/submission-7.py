class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # normal bellman-ford 
        dist = [float('inf')] * n
        dist[src] = 0
        
        # Relax K + 1 times (K stops = K + 1 edges)
        for _ in range(k + 1):
            tmp_dist = dist[:] # Create a snapshot of previous results
            for u, v, w in flights:
                if dist[u] != float('inf'):
                    tmp_dist[v] = min(tmp_dist[v], dist[u] + w)
            dist = tmp_dist # Update the main distances after the "layer" is processed
            
        return dist[dst] if dist[dst] != float('inf') else -1