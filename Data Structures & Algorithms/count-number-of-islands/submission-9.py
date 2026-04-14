class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0]) # row, col 
        visited = [[False] * n for _ in range(m)] # every node is unvisited first 
        directions = [(1,0), (0,1), (-1,0), (0,-1)] # x and y direction move 1 or -1 
        res = 0 

        # purpose of this BFS: when encounter a land for first time 
        # keep BFS its neighbor to find the entire island
        def bfs(x, y):
            # use queue to keep track of visited node 
            queue = collections.deque([])
            # whenever a node is added to queue, mark it as visited
            queue.append((x,y))
            visited[x][y] = True 

            # keep iterating through queue, keep add each node's land neighbor in 4 directions to queue 
            # once queue is empty, all neighbor land are visited 
            while queue:
                # get the x, y coordinate of current node 
                curX, curY = queue.popleft()
                # get dx, dy in all 4 directions
                for dx, dy in directions:
                    nextX, nextY = curX + dx, curY + dy 
                    # nextX and nextY can't be out of bond, skip if yes
                    if nextX < 0 or nextY < 0 or nextX >= m or nextY >= n:
                        continue 
                    # if valid, only append to queue if current node is an unvisited land 
                    if grid[nextX][nextY] == "1" and not visited[nextX][nextY]:
                        queue.append((nextX, nextY))
                        # whenever a node is added to queue, mark it as visited
                        visited[nextX][nextY] = True 
                        # then do BFS on this new land again 
                        bfs(nextX, nextY)
                
        for i in range(m):
            for j in range(n):
                # when countered an unvisited land, add 1 to res 
                if grid[i][j] == "1" and not visited[i][j]:
                    res += 1
                    # use bfs to find remaining connecting land
                    bfs(i, j)
        
        return res 
                    
