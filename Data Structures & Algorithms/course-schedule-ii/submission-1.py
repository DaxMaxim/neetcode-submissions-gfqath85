class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {i : [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for crs, pre in prerequisites:
            adjList[pre].append(crs)
            indegree[crs] += 1
        
        que = deque(i for i in range(numCourses) if indegree[i] == 0)
        top = []

        while que:
            crs = que.popleft()

            for nei in adjList[crs]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    que.append(nei)
            top.append(crs)
        return top if len(top) == numCourses else []