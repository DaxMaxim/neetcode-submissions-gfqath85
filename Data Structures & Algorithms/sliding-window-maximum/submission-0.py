class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()
        l, r = 0, 0

        while r < len(nums):
            
            # pop values smaller than q and then append
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if r-l+1 == k: 
                output.append(nums[q[0]])
                if nums[l] == nums[q[0]]:
                    q.popleft()
                l += 1
            r += 1
        return output