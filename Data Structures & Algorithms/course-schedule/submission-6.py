class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegree = [0] * numCourses 
        adj = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            adj[u].append(v)
            inDegree[v] += 1
        
        queue = collections.deque() # for course with 0 prereq
        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)
        
        taken = 0 
        while queue:
            u = queue.popleft()
            taken += 1
            for v in adj[u]:
                inDegree[v] -= 1
                if inDegree[v] == 0:
                    queue.append(v)
        return taken == numCourses