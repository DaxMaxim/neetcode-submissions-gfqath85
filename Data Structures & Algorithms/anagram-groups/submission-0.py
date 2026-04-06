class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for st in strs:
            freq = [0]*26
            for s in st:
                freq[ord(s)-ord("a")] += 1
            groups[tuple(freq)].append(st)
        return list(groups.values())