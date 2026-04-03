class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Dijkstra
        # 1. Build the Adjacency List: {from: [(to, price), ...]}
        adj = collections.defaultdict(list)
        for u, v, w in flights:
            adj[u].append((v, w))
        
        # 2. Priority Queue: (cost, current_node, stops_spent)
        # We use cost first so the heap stays a Min-Heap based on price
        pq = [(0, src, 0)]
        
        # 3. Track the fewest stops used to reach each node
        # If we reach a node with more stops than recorded, it's a worse path
        stops_record = [float('inf')] * n
        
        while pq:
            cost, u, stops = heapq.heappop(pq)
            
            # If we've exceeded the allowed stops or found a path to 'u' 
            # that took fewer stops previously, skip this branch.
            if stops > k + 1 or stops > stops_record[u]:
                continue
            
            # Update the minimum stops for this node
            stops_record[u] = stops
            
            # If we reached the destination, because it's a Min-Heap,
            # the first time we pop 'dst', it's the cheapest valid path.
            if u == dst:
                return cost
            
            # Explore neighbors
            for v, weight in adj[u]:
                heapq.heappush(pq, (cost + weight, v, stops + 1))
                
        return -1