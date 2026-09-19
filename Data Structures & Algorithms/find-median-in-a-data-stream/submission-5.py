class MedianFinder:

    def __init__(self):
        self.maxHeap, self.minHeap = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -num)

        # make sure each element in the max heap is less than elements in min heap
        if self.maxHeap and self.minHeap and -self.maxHeap[0] > self.minHeap[0]:
            n = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -n)

        # balancing the sizes
        if len(self.maxHeap) > len(self.minHeap) + 1:
            n = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -n)
        elif len(self.minHeap) > len(self.maxHeap) + 1:
            n = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -n)
          
    def findMedian(self) -> float:

        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        
        return (self.minHeap[0] + (-self.maxHeap[0])) / 2
        



        
        