class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float('inf')
        adj = [[] for _ in range(n)] # adjacency list
        minDist = [[INF] * (k + 5) for _ in range(n)] # min distance of each node to origin 
        for frm, to, cost in flights:
            adj[frm].append([to, cost])
        
        minDist[src][0] = 0 
        minHeap = [(0, src, -1)] # cost, node, stops
        while len(minHeap):
            cost, node, stops = heapq.heappop(minHeap)
            if dst == node: return cost 
            if stops == k or minDist[node][stops + 1] < cost:
                continue 
            
            for neighbor, weight in adj[node]:
                nextCost = cost + weight 
                nextStops = 1 + stops 
                if minDist[neighbor][nextStops + 1] > nextCost:
                    minDist[neighbor][nextStops + 1] = nextCost
                    heapq.heappush(minHeap, (nextCost, neighbor, nextStops))
        
        return -1 