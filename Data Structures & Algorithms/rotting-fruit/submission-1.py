class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = collections.deque() # (i,j) of rotten orange
        count_fresh = 0 # count of fresh orange
        # populate queue 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count_fresh += 1
                if grid[i][j] == 2:
                    queue.append((i,j))
        
        # check edge case 
        if not count_fresh:
            return 0 
        if not queue:
            return -1 

        time = -1 
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while queue:
            size = len(queue) # num of rotten orange at current time 
            while size > 0:
                x, y = queue.popleft() # pop one rotten orange
                size -= 1 
                # infect in 4 directions
                for dx, dy in directions:
                    i, j = x + dx, y + dy 
                    # check bondary of i, j and fresh 
                    if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                        # one fresh got rotten
                        grid[i][j] = 2
                        count_fresh -= 1
                        # append rotten to queue 
                        queue.append((i,j))
            # after all rotten orange at current time finish infections 
            time += 1
        
        if count_fresh == 0:
            return time 
        else:
            return -1 

                        