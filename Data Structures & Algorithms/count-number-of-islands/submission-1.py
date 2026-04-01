class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        res = 0 
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def bfs(x, y):
            queue = collections.deque([(x,y)])
            visited[x][y] = True 

            while queue:
                cur_x, cur_y = queue.popleft()
                for dx, dy in directions:
                    next_x = cur_x + dx 
                    next_y = cur_y + dy 
                    if next_x < 0 or next_y < 0 or next_x >= m or next_y >= n:
                        continue 
                    if grid[next_x][next_y] == "1" and not visited[next_x][next_y]:
                        visited[next_x][next_y] = True 
                        queue.append((next_x, next_y))
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    res += 1
                    bfs(i, j)
        
        return res 


