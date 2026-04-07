class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Core idea:先上没有任何前置课的课，也就是入度为0的node。此课上完后，将它从链接的
        # 所有后置课程中去除，直到所有课都上过
        indegree = [0] * numCourses # inDegree 记录每个课程的入度(有多少prerequite)
        adj = [[] for _ in range(numCourses)]
        for src, dst in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)

        # 初始化队列，加入所有入度为0的节点
        queue = collections.deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        finished = 0 # 记录上了多少节课
        while queue:
            node = queue.popleft() # 当前没有前置的课程
            finished += 1 # 上完的课数量+1
            for nei in adj[node]: # 寻找所有后置课程
                indegree[nei] -= 1 # 因为当前课已上完，所以后置课程的入度-1
                if indegree[nei] == 0: # 如果后置课程没有入度，说明可以上这个课了
                    queue.append(nei) # 加入此后置课程队列
        
        return finished == numCourses