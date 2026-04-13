class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def bfs(x, y):
            queue = collections.deque()
            queue.append((x, y))
            visited[x][y] = True

            while queue:
                curX, curY = queue.popleft()
                for dx, dy in directions:
                    i, j = curX + dx, curY + dy 
                    if i < 0 or j < 0 or i >= m or j >= n:
                        continue 
                    if not visited[i][j] and grid[i][j] == "1":
                        queue.append((i, j))
                        visited[i][j] = True 
                        bfs(i, j)
        res =0 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    res += 1
                    bfs(i, j)
        
        return res 


