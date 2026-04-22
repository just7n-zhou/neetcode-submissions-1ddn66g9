class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        # when meet a land, do bfs to find its perimeter
        # since there is only one land, so only do BFS once
        def bfs(i, j):
            queue = collections.deque()
            queue.append((i, j)) # store land (i, j)
            visited[i][j] = True 
            perimeter = 0 # initialize the land's perimeter

            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    # check current land's 4 directions 
                    nx, ny = x + dx, y + dy 
                    # if this direction is out of bond or meet a water 
                    # meaning current side's direction is an edge and count for perimeter
                    if nx < 0 or ny < 0 or nx >= m or ny >= n or grid[nx][ny] == 0:
                        perimeter += 1 
                    # if this direction leads to another land, then it's not edge, 
                    # so don't count for perimeter 
                    elif not visited[nx][ny] and grid[nx][ny] == 1:
                        # add new land to queue for furthur traverse
                        queue.append((nx, ny))
                        visited[nx][ny] = True 
            # after this bfs perimeter is found
            return perimeter 

        # traverse to find the first land piece 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # do bfs if found 
                    return bfs(i, j)
    
        return 0 