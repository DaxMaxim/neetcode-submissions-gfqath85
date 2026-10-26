class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq, visit = defaultdict(list), set()

        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        def dfs(crs_num):
            if not prereq[crs_num]: return True
            if crs_num in visit: return False

            visit.add(crs_num)

            for nei in prereq[crs_num]:
                if not dfs(nei): return False

            prereq[crs_num] = []
            return True

        for crs_num in range(numCourses):
            if not dfs(crs_num): return False
        return True