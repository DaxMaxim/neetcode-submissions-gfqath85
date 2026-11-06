class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList, res = defaultdict(list), []
        cycle, visited = set(), set()

        for crs, pre in prerequisites:
            adjList[crs].append(pre)

        def dfs(crs_num):
            if crs_num in cycle: return False
            if crs_num in visited: return True
            
            cycle.add(crs_num)
            visited.add(crs_num)

            for nei in adjList[crs_num]:
                if not dfs(nei): return False
            
            cycle.remove(crs_num)
            res.append(crs_num)
            return True

        for crs_num in range(numCourses):
            if not dfs(crs_num): return []
        return res

        