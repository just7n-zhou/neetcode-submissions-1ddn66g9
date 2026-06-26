class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def bfs(i,j):
            queue = collections.deque()
            queue.append((i, j))
            visited[i][j] = True 

            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nX, nY = x + dx, y + dy 
                    if nX < 0 or nY < 0 or nX >= m or nY >= n:
                        continue 
                    if grid[nX][nY] == "1" and not visited[nX][nY]:
                        queue.append((nX, nY))
                        visited[nX][nY] = True 
        
        res = 0 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    res += 1
                    bfs(i, j)
        
        return res 