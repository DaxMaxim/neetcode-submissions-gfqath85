class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        
        cycle, visited, output = set(), set(), []

        def dfs(num):
            if num in cycle: return False
            if num in visited: return True

            cycle.add(num)
            for nei in prereq[num]:
                if not dfs(nei): return False
            visited.add(num)
            output.append(num)
            cycle.remove(num)
            return True

        for num in range(numCourses):
            if not dfs(num): return []
        return output