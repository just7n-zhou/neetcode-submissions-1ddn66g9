class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        minPrices = [float('inf')] * n 
        minPrices[src] = 0

        for _ in range(k + 1):
            tempPrices = minPrices.copy()
            for u, v, price in flights:
                if minPrices[u] != float('inf'):
                    if minPrices[u] + price < tempPrices[v]:
                        tempPrices[v] = minPrices[u] + price
            minPrices = tempPrices
        
        return minPrices[dst] if minPrices[dst] != float('inf') else -1 
