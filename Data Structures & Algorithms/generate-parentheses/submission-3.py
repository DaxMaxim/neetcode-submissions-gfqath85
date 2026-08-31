class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(curr_path, opn, close):
            if opn == close == n:
                res.append("".join(curr_path))
                return
            
            if opn < n:
                curr_path.append("(")
                dfs(curr_path, opn + 1, close)
                curr_path.pop()

            if close < opn:
                curr_path.append(")")
                dfs(curr_path, opn, close + 1)
                curr_path.pop()
            
        dfs([], 0, 0)
        return res