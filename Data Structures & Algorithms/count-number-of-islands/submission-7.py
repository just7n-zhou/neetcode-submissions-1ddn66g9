class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def bfs(i, j):
            queue = collections.deque()
            queue.append((i, j))
            visited[i][j] = True 

            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nextX, nextY = x + dx, y + dy 
                    # bondary check 
                    if nextX < 0 or nextY < 0 or nextX >= m or nextY >= n:
                        continue 
                    # check if it's a unvisited land 
                    if not visited[nextX][nextY] and grid[nextX][nextY] == "1":
                        queue.append((nextX, nextY))
                        visited[nextX][nextY] = True 
                        bfs(nextX, nextY)
        
        # look for land
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    res += 1
                    bfs(i, j)
        
        return res 

