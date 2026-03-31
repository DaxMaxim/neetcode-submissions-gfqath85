class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        
        cycle, visited = set(), set()

        def dfs(num):
            if num in cycle: return False
            if num in visited: return True

            cycle.add(num)
            
            for nei in prereq[num]:
                if not dfs(nei): return False
            cycle.remove(num)
            visited.add(num)
            return True

        for num in range(numCourses):
            if not dfs(num): return False
        return True