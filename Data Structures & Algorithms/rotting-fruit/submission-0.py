class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = collections.deque() # (x, y) for rotten orange 
        count_fresh = 0 # num of fresh orange
        # populate queue and count_fresh
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    count_fresh += 1
        
        # edge case: no rotten or no fresh 
        if not count_fresh:
            return 0 
        if not queue:
            return -1 
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        # when all orange are rotten, queue still not empty 
        # and will process one last time, so time should be -1 initially
        time = -1
        while queue:
            size = len(queue) # keep track of rotten at current instant
            while size > 0: 
                # pop one rotten at a time until size is empty
                x, y = queue.popleft() 
                size -= 1 
                # rot oranges in 4 directions
                for dx, dy in directions:
                    i, j = x + dx, y + dy 
                    # check i, j boundary and if current location is a fresh orange
                    if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                        grid[i][j] = 2 # fresh got rotten
                        count_fresh -= 1  
                        queue.append((i, j)) # append rotten to queue 
            # rotten happens instantly, only add 1 after all rot orange at current instant finish infections 
            time += 1
        
        # if all rotten finished infection and there are still fresh orange left, return -1 
        if count_fresh != 0:
            return -1
        else:
            return time 

