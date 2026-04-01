class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in flights:
            adj[u].append((v, w))
        
        minStops = [float("inf")] * n
        pq = [(0, src, 0)]

        while pq:
            cost, u, stops = heapq.heappop(pq)

            if stops > k + 1 or stops > minStops[u]:
                continue 
            
            minStops[u] = stops 

            if u == dst:
                return cost 
            
            for v, weight in adj[u]:
                heapq.heappush(pq, (cost + weight, v, stops + 1))
        
        return -1 

