class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset, visit = set(nums), set()
        res = 0
        for num in numset:
            if num in visit: continue
            visit.add(num)
            countL, countR = 0, 0 

            # go right
            start = num
            while (start + 1) in numset:
                countR += 1
                start += 1
            start = num
            while (start - 1) in numset:
                countL += 1
                start = start - 1
            res = max(res, countL + countR + 1)
        return res
        
            

            
