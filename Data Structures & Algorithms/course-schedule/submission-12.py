class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        cycle, visit = set(), set()
        adjList = defaultdict(list)

        for crs, prereq in prerequisites:
            adjList[crs].append(prereq)

        def dfs(crs):
            if crs in cycle: return False
            if crs in visit: return True

            cycle.add(crs)

            for nei in adjList[crs]:
                if not dfs(nei): return False

            visit.add(crs)
            cycle.remove(crs)
            return True
        
        for crs_num in range(numCourses):
            if not dfs(crs_num): return False
        return True