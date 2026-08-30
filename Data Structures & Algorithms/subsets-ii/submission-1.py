class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, curr_path):
            if i >= len(nums):
                res.append(curr_path.copy())
                return
            
            curr_path.append(nums[i])
            dfs(i + 1, curr_path)
            curr_path.pop()

            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            dfs(i + 1, curr_path)
        dfs(0, [])
        return res