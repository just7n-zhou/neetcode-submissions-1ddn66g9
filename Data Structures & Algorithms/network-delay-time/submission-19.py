class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Bellman-ford
        # 1. Initialize distances from source k to all nodes
        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        
        # 2. Relax all edges n-1 times
        # 对所有边松弛一次，相当于计算 起点到达 与起点一条边相连的节点 的最短距离
        # 松弛两次，就找到 与起点两条边相连的节点 的最短距离
        # n个节点的图最多有n-1个边， 所以n-1次一定能到任何终点
        for _ in range(n - 1):
            updated = False
            for u, v, w in times:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    updated = True
            
            # Optimization: If no distances changed in an entire pass, we are done
            if not updated:
                break
                
        # 3. Final result logic
        max_dist = max(dist[1:])
        return max_dist if max_dist != float('inf') else -1