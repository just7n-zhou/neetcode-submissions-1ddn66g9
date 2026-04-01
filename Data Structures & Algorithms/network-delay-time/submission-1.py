import collections
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 1. Build adjacency list: {source: [(destination, weight), ...]}
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        # 2. minHeap stores (total_time_from_k, current_node)
        # Starting point k has 0 time cost
        minHeap = [(0, k)]
        
        # 3. Use a set to keep track of finalized nodes
        visit = set()
        
        # 't' will track the time of the latest node popped from the heap
        t = 0
        
        while minHeap:
            # Always pop the node with the absolute smallest time cost
            w1, n1 = heapq.heappop(minHeap)
            
            # If we've already finalized this node via a shorter path, skip it
            if n1 in visit:
                continue
            
            # Finalize the node
            visit.add(n1)
            
            # Since Dijkstra pops nodes in increasing order of time, 
            # the last node popped will have the maximum 'shortest path' time.
            t = w1

            # Check all neighbors of the current node
            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    # Push the cumulative time to reach the neighbor
                    heapq.heappush(minHeap, (w1 + w2, n2))
        
        # If the number of unique visited nodes equals n, return the last time 't'.
        # Otherwise, at least one node was unreachable.
        return t if len(visit) == n else -1