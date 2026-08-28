class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq, q = {}, deque()
        cycles = 0

        for task in tasks:
            freq[task] = 1 + freq.get(task, 0)
        
        tasks = []
        for task in freq:
            tasks.append([-freq[task], task, float("inf")])
        heapq.heapify(tasks)

        while tasks or q:
            cycles += 1

            while q and cycles - q[0][2] > n:
                ready_task = q.popleft()
                heapq.heappush(tasks, ready_task)
            
            if tasks:
                most_freq_task = heapq.heappop(tasks)
                most_freq_task[0] += 1
                if most_freq_task[0] < 0:
                    most_freq_task[2] = cycles
                    q.append(most_freq_task)
          
        return cycles


                
        



        