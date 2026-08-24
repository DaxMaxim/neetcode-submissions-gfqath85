class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k, self.minHeap = k, nums
        heapq.heapify(self.minHeap)

        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        if len(self.minHeap) < self.k:
            heapq.heappush(self.minHeap, val)
        elif val > self.minHeap[0]:
            heapq.heappush(self.minHeap, val)
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
        

