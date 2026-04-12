class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {i : [] for i in range(n)}
        for first, sec in edges:
            adjList[first].append(sec)
            adjList[sec].append(first)

        visit, res = set(), 0

        def dfs(num):
            visit.add(num)
            for nei in adjList[num]:
                if nei not in visit: dfs(nei)
            return

        for num in range(n):
            if num not in visit:
                dfs(num)
                res += 1
        return res