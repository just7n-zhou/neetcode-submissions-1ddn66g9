class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # normal bellman-ford 
        minPrices = [float('inf')] * n
        minPrices[src] = 0
        
        # Relax K + 1 times (K stops = K + 1 edges)
        for _ in range(k + 1):
            # need previous iteration's result to avoid extra stops between one node to another
            # this force algo to only extend path by only one edge per iteration 
            tempPrices = minPrices.copy() # Create a snapshot of previous results
            for u, v, cost in flights:
                # if cost to reach U is infinity then V it's not reachable, skip it 
                if minPrices[u] != float('inf'):
                    # compare the sum of cost to reach U from previous resuls and cost from U to V 
                    # with the cost to reach V at current temp prices 
                    if minPrices[u] + cost < tempPrices[v]:
                        tempPrices[v] = minPrices[u] + cost
            minPrices = tempPrices # Update the main distances after the "layer" is processed
            
        return minPrices[dst] if minPrices[dst] != float('inf') else -1