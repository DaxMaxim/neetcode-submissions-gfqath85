class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # make an adjecency list
        adjList = {i: [] for i in range(n)}

        for first, sec in edges:
            adjList[first].append(sec)
            adjList[sec].append(first)

        cycle = set()
        # do dfs, check for cycle
        def dfs(node, prev):
            if node in cycle: return False
            
            cycle.add(node)
            for nb in adjList[node]:
                if nb == prev: continue
                if not dfs(nb, node): return False
            return True

        return dfs(0, -1) and len(cycle) == len(adjList)
