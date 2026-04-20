class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0]) # row, col 
        visited = [[False] * n for _ in range(m)]

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def bfs(x, y):
            queue = collections.deque([])
            queue.append((x, y))
            visited[x][y] = True 

            while queue:
                curX, curY = queue.popleft()
                for dx, dy in directions:
                    nxtX, nxtY = curX + dx, curY + dy 
                    if nxtX < 0 or nxtX >= m or nxtY < 0 or nxtY >= n:
                        continue 
                    if not visited[nxtX][nxtY] and grid[nxtX][nxtY] == "1":
                        queue.append((nxtX, nxtY))
                        visited[nxtX][nxtY] = True 
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    res += 1
                    bfs(i, j)
        
        return res 