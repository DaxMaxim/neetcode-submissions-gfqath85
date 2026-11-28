class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        cycle, visit = set(), set()
        adjList = defaultdict(list)
        res = []

        for crs, prereq in prerequisites:
            adjList[crs].append(prereq)
        
        def dfs(crs):
            if crs in cycle: return False
            if crs in visit: return True

            cycle.add(crs)

            for nei in adjList[crs]:
                if not dfs(nei): return False

            res.append(crs)
            cycle.remove(crs)
            visit.add(crs)
            return True

        for crs_num in range(numCourses):
            if not dfs(crs_num): return []
        return res