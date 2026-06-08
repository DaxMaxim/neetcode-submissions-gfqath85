class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]*len(nums)

        product = 1
        for i in range(len(nums)):
            pre[i] = product
            product = product * nums[i]
        
        product = 1
        for i in range(len(nums)-1, -1, -1):
            tmp = nums[i]
            nums[i] = product
            product = product * tmp
        
        for i in range(len(nums)):
            nums[i] *= pre[i]
        return nums
