class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)
        freq1, freq2 = {}, {}
        for ele in s:
            freq1[ele] = 1 + freq1.get(ele, 0)
        for ele in t:
            freq2[ele] = 1 + freq2.get(ele, 0)
        return freq1 == freq2