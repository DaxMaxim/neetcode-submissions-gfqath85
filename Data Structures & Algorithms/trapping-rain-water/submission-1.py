class Solution:
    def trap(self, height: List[int]) -> int:
        maxL, maxR = height[0], height[-1]
        max_area = 0

        l, r = 0, len(height)-1
        while l < r:
            if height[l] <= height[r]:
                water = max(0, maxL - height[l])
                maxL = max(maxL, height[l])
                l += 1
            else:
                water = max(0, maxR - height[r])
                maxR = max(maxR, height[r])
                r -= 1
            max_area += water
        return max_area

