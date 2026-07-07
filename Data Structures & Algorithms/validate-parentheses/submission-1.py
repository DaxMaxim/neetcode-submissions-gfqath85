class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {")":"(", "]":"[", "}":"{"}
        
        for br in s:
            # closing bracket
            if br in close_to_open:
                if not stack or stack[-1] != close_to_open[br]: return False
                stack.pop()
            else:
                stack.append(br)
        return True if not stack else False

