class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickselect(low, high):
            # if low >= high: return
            pivot, i = nums[high], low

            for j in range(low, high):
                if nums[j] <= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[high], nums[i] = nums[i], nums[high]

            if i > k:
                return quickselect(low, i - 1)
            elif i < k:
                return quickselect(i + 1, high)
            else:
                return nums[i]
        return quickselect(0, len(nums)-1)

