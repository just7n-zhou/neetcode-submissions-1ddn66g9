class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        queue = collections.deque()
        count_fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    count_fresh += 1
        
        if count_fresh == 0:
            return 0 
        if not queue:
            return -1 

        
        time = -1
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while queue:
            size = len(queue)
            while size > 0:
                x, y = queue.popleft()
                size -= 1
                for dx, dy in directions:
                    nxtX, nxtY = x + dx, y + dy 
                    if 0 <= nxtX < m and 0 <= nxtY < n:
                        if not visited[nxtX][nxtY] and grid[nxtX][nxtY] == 1:
                            grid[nxtX][nxtY] = 2 
                            visited[nxtX][nxtY] = True
                            count_fresh -= 1
                            queue.append((nxtX, nxtY))
            time += 1
        
        if count_fresh != 0:
            return -1 
        else:
            return time