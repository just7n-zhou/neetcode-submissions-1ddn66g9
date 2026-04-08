class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegree = [0] * numCourses 
        adj = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            adj[u].append(v)
            inDegree[v] += 1
        
        queue = collections.deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)
        
        finished = 0 
        while queue:
            course = queue.popleft()
            finished += 1
            for post in adj[course]:
                inDegree[post] -= 1
                if inDegree[post] == 0:
                    queue.append(post)
        
        return finished == numCourses