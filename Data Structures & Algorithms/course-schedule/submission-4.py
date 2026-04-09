class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # keep track of num of prereq of each course 
        indegree = [0] * numCourses 
        # build adjacency list
        adj = [[] for _ in range(numCourses)]
        # fill indegree map and adj list
        for u, v in prerequisites:
            adj[u].append(v)
            indegree[v] += 1
        
        # queue to track all course without prereq
        queue = collections.deque()
        for course in range(numCourses):
            if indegree[course] ==0:
                queue.append(course)

        # whenever a course popped from queue, it's taken
        taken = 0
        while queue:
            u = queue.popleft()
            taken += 1
            # iterate all courses that use current u as prereq
            for v in adj[u]:
                # the course v prereq -1 
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
        
        return taken == numCourses 
        
