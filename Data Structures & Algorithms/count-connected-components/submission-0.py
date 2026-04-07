class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visited=[False] * n
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def bfs(node):
            q = collections.deque([node])
            visited[node] = True 
            while q:
                cur = q.popleft()
                for neighbor in adj[cur]:
                    if not visited[neighbor]:
                        visited[neighbor] = True 
                        q.append(neighbor)
        
        res = 0 
        for node in range(n):
            if not visited[node]:
                res += 1
                bfs(node)
        
        return res 