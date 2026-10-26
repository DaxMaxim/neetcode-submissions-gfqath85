class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq, path, visited = defaultdict(list), set(), set()

        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        def dfs(crs_num):
            if crs_num in visited: return True
            if crs_num in path: return False

            path.add(crs_num)

            for nei in prereq[crs_num]:
                if not dfs(nei): return False

            # path.remove(crs_num)
            visited.add(crs_num)
            return True

        for crs_num in range(numCourses):
            if not dfs(crs_num): return False
        return True

        # what would happen if I don't remove from my path.