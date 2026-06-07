class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(nlog(n) solution
        # freq, res = {}, []
        # for num in nums:
        #     freq[num] = 1 + freq.get(num, 0)
        # l = list(freq.items())
        # l.sort(key = lambda x: x[1], reverse=True)
        # for i in range(0, k):
        #     res.append(l[i][0])
        # return res

        # O(n) solution
        freq, res = {}, []
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        bucket = [[] for i in range(len(nums) + 1)]

        for num, frq in freq.items():
            bucket[frq].append(num)
        
        for i in range(len(nums), -1, -1):
            for n in bucket[i]:
                res.append(n)
                k -= 1
                if k == 0: return res
