class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        area = 0 
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(i, j):
            queue = deque()
            grid[i][j] = 0 
            queue.append((i, j))
            res = 1 

            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy 
                    if nx < 0 or ny < 0 or nx >=m or ny >= n or grid[nx][ny] == 0:
                        continue 
                    queue.append((nx, ny))
                    grid[nx][ny] = 0 
                    res += 1
            return res 

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = max(area, bfs(i, j))
        
        return area 