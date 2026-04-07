class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses # check prerequite of each course 
        # build adj list 
        adj = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            adj[u].append(v)
            indegree[v] += 1
        
        # a queue to store all courses without prerequite
        queue = collections.deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        finished = 0 # track how many courses have taken
        while queue:
            # taken current course without prerequite
            u = queue.popleft()
            finished += 1 
            # for each next course connected to current course
            for v in adj[u]:
                # subtract their prerequite by 1
                indegree[v] -= 1
                # if this next course has no prerequite, add to queue
                if indegree[v] == 0:
                    queue.append(v)
        
        return finished == numCourses 