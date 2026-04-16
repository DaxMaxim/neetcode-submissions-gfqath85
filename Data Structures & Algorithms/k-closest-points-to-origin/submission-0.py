class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heap = [(math.dist((0, 0), (ele[0], ele[1])), ele) for ele in points]
        heapq.heapify(heap)
        while k > 0:
            dist, coor = heapq.heappop(heap)
            res.append(coor)
            k -= 1
        return res