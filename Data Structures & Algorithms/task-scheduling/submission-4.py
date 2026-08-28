class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq, q = {}, deque()
        cycles = 0

        for task in tasks:
            freq[task] = 1 + freq.get(task, 0)
        
        tasks = [-frq for frq in freq.values()]
        heapq.heapify(tasks)

        while tasks or q:
            cycles += 1

            if tasks:
                frq = 1 + heapq.heappop(tasks)
                if frq < 0:
                    q.append([frq, cycles + n])

            while q and cycles == q[0][1]:
                heapq.heappush(tasks, q.popleft()[0])
        return cycles


                
        



        