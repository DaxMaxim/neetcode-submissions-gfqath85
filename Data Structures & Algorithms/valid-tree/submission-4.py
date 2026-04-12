class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {i:[] for i in range(n)}

        for first, sec in edges:
            adjList[first].append(sec)
            adjList[sec].append(first)

        cycle, visited = set(), set()
        
        def dfs(num, prev):
            if num in cycle: return False

            cycle.add(num)
            visited.add(num)
            for nei in adjList[num]:
                if nei == prev: continue
                if not dfs(nei, num): return False
            cycle.remove(num)
            return True
        
        if not dfs(0, -1): return False

        for num in range(n):
            if num not in visited: return False
        return True
        