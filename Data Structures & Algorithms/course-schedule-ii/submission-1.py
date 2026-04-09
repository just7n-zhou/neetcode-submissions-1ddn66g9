class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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
        # output course array but in reversed order 
        # since in prerequisites array is course[prerequites]
        res = []
        while queue:
            u = queue.popleft()
            taken += 1
            res.append(u)
            # iterate all courses that use current u as prereq
            for v in adj[u]:
                # the course v prereq -1 
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
        
        # if all courses are taken, return reversed output array 
        if taken == numCourses:
            return res[::-1]
        else:
            return [] 