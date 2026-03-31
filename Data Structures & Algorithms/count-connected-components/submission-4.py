class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set()
        adjList = defaultdict(list)
        components = 0

        def dfs(node):
            visit.add(node)
            for nb in adjList[node]:
                if nb not in visit:
                    dfs(nb)
        # form an adjecency list
        for node1, node2 in edges:
            adjList[node1].append(node2)
            adjList[node2].append(node1)
        # traverse on it to find number of components
        for node in range(n):
            if node in visit: continue
            dfs(node)
            components += 1
        return components