class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        eleset = set()
        for num in nums:
            if num in eleset: return True
            eleset.add(num)
        return False