class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_time = [ [p, (target-p)/s] for p, s in zip(position, speed)]
        stack, count = [], 0

        pos_time.sort()
        for i in range(len(pos_time)-1, -1, -1):
            stack.append(pos_time[i][1])
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

            