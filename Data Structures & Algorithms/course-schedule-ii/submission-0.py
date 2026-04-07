class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses 
        adj = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            adj[u].append(v)
            indegree[v] += 1
        
        queue = collections.deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        finished = 0
        output = []
        while queue:
            course = queue.popleft()
            finished += 1
            output.append(course)
            for post in adj[course]:
                indegree[post] -= 1
                if indegree[post] == 0:
                    queue.append(post)
        
        if len(output) == numCourses:
            return output[::-1]
        else:
            return []