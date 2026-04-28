class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = 2147483647

        def bfs(i, j):
            queue = deque([(i, j)])
            visited = [[False] * COLS for _ in range(ROWS)]
            visited[i][j] = True 
            steps = 0 
            while queue:
                for _ in range(len(queue)):
                    x, y = queue.popleft()
                    if grid[x][y] == 0:
                        return steps 
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy 
                        if (0 <= nx < ROWS and 0 <= ny < COLS and
                                not visited[nx][ny] and grid[nx][ny] != -1):
                                visited[nx][ny] = True 
                                queue.append((nx, ny))
                steps += 1 

            return INF
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == INF:
                    grid[i][j] = bfs(i, j)