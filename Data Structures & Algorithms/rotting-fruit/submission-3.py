class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = collections.deque()
        count_fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count_fresh += 1
                if grid[i][j] == 2:
                    queue.append((i, j))
        
        if not count_fresh:
            return 0 
        if not queue:
            return -1 

        time = -1 
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        while queue:
            size = len(queue)
            while size > 0:
                x, y = queue.popleft()
                size -= 1
                for dx, dy in directions:
                    i, j = x + dx, y + dy 
                    if i < 0 or i >= m or j < 0 or j >= n:
                        continue 
                    if grid[i][j] == 1:
                        grid[i][j] = 2
                        count_fresh -= 1
                        queue.append((i,j))
            time += 1
        
        if count_fresh != 0:
            return -1 
        return time 
