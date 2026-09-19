class MedianFinder:

    def __init__(self):
        self.maxHeap, self.minHeap = [], []

    def addNum(self, num: int) -> None:
        if not self.maxHeap:
            heapq.heappush(self.maxHeap, -num)
        elif -num < self.maxHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)

        if len(self.minHeap) - len(self.maxHeap) > 0:
            num = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -num) 
        elif len(self.maxHeap) - len(self.minHeap) > 1:
            num = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -num)
          
    def findMedian(self) -> float:
        total_len = len(self.maxHeap) + len(self.minHeap)

        if total_len % 2:
            return -self.maxHeap[0]
        else:
            first = self.minHeap[0]
            sec = -self.maxHeap[0]

            return (first + sec) / 2
        