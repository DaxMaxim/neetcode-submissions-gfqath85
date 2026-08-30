class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, curr_path, total):
            if total == target:
                res.append(curr_path.copy())
                return
            if i >= len(candidates) or total > target:
                return

            curr_path.append(candidates[i])
            dfs(i + 1, curr_path, total + candidates[i])
            curr_path.pop()

            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i = i + 1
            dfs(i + 1, curr_path, total)

        dfs(0, [], 0)
        return res