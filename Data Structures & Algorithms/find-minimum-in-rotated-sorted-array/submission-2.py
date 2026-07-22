class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0 , len(nums)-1
        min_num = float("inf")

        while l <= r:
            if nums[l] < nums[r]:
                return min(nums[l], min_num)

            mid = (l + r) // 2

            # left half
            if nums[mid] >= nums[l] and nums[mid] > nums[r]:
                l = mid + 1
            # right half
            else:
                r = mid - 1
            
            min_num = min(min_num, nums[mid])
        return min_num