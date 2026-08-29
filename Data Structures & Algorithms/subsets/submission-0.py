class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, curr_path):
            if i >= len(nums): 
                res.append(curr_path.copy())
                return
            
            dfs(i + 1, curr_path)
            curr_path.append(nums[i])
            dfs(i + 1, curr_path)
            curr_path.pop()
        dfs(0, [])
        return res