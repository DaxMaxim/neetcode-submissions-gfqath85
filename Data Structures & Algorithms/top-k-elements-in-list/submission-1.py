class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq, res = {}, []
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        l = list(freq.items())
        l.sort(key = lambda x: x[1], reverse=True)
        for i in range(0, k):
            res.append(l[i][0])
        return res

