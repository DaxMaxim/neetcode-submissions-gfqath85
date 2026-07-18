class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack, maxArea = [], 0
        left, right = [0] * len(heights), [len(heights)-1] * len(heights)

        # left to right pass
        for i in range(len(heights)):
            while stack and heights[i] < stack[-1][0]:
                num, indx = stack.pop()
                right[indx] = i - 1
            stack.append([heights[i], i])
        
        stack = []

        # right to left pass
        for i in range(len(heights)-1, -1, -1):
            while stack and heights[i] < stack[-1][0]:
                num, indx = stack.pop()
                left[indx] = i + 1
            stack.append([heights[i], i])
        
        for i in range(len(heights)):
            area = (right[i] - left[i] + 1) * heights[i]
            maxArea = max(maxArea, area)
        return maxArea
        



