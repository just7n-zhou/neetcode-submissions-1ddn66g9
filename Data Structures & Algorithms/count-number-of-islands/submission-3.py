class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n  = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        directions = [(1,0),(0, 1),(-1,0),(0,-1)]
        res = 0 

        def bfs(x, y):
            queue = collections.deque([])
            queue.append((x,y))
            visited[x][y] = True 

            while queue:
                curX, curY = queue.popleft()
                for dx, dy in directions:
                    nextX, nextY = curX + dx, curY + dy
                    if nextX < 0 or nextY < 0 or nextX >= m or nextY >= n:
                        continue 
                    if grid[nextX][nextY] == "1" and not visited[nextX][nextY]:
                        queue.append((nextX, nextY))
                        visited[nextX][nextY] = True 
                        bfs(nextX, nextY)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    res += 1
                    bfs(i, j)
        
        return res 