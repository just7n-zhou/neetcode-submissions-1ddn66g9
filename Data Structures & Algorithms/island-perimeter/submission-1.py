class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def bfs(i, j):
            queue = collections.deque()
            queue.append((i, j))
            visited[i][j] = True 
            perimeter = 0 

            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy 
                    if nx < 0 or ny < 0 or nx >= m or ny >= n or grid[nx][ny] == 0:
                        perimeter += 1 
                    elif not visited[nx][ny] and grid[nx][ny] == 1:
                        queue.append((nx, ny))
                        visited[nx][ny] = True 
            return perimeter 
    
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return bfs(i, j)
    
        return 0 