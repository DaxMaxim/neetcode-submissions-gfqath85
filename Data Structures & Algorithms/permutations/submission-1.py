class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, curr_path = [], set()

        def dfs(i, curr_list):
            if i >= len(nums):
                res.append(curr_list.copy())
                return
            
            for num in nums:
                if num in curr_path: continue
                curr_path.add(num)
                curr_list.append(num)

                dfs(i + 1, curr_list)

                curr_list.remove(num)
                curr_path.remove(num)
        dfs(0, [])
        return res
