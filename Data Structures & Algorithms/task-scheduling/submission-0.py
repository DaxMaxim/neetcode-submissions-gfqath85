class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        vals = list(freq.values())
        vals = [-x for x in vals]
        heapq.heapify(vals)
        que, time = deque(), 0

        while vals or que:
            time += 1
            if vals:
                num_count = heapq.heappop(vals)
                if num_count < -1: que.append((num_count + 1, time + n))
            if que and que[0][1] == time:
                heapq.heappush(vals, que.popleft()[0])
        return time