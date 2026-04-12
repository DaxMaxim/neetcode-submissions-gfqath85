class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {i:[] for i in range(n)}

        for first, sec in edges:
            adjList[first].append(sec)
            adjList[sec].append(first)

        cycle = set()
        
        def dfs(num, prev):
            if num in cycle: return False

            cycle.add(num)
            for nei in adjList[num]:
                if nei == prev: continue
                if not dfs(nei, num): return False
            return True
        
        if (not dfs(0, -1)) or (len(cycle) != n): return False
        return True
        