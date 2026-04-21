class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegree = [0] * numCourses 
        adj = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            adj[u].append(v)
            inDegree[v] += 1
        
        queue = collections.deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)
        
        taken = 0
        order = []
        while queue:
            u = queue.popleft()
            taken += 1
            order.append(u)
            for v in adj[u]:
                inDegree[v] -= 1
                if inDegree[v] == 0:
                    queue.append(v)
        
        return order[::-1] if taken == numCourses else []