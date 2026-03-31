class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for st in strs:
            s += str(len(st)) + "#" + st
        return s

    def decode(self, s: str) -> List[str]:
        l = r = 0
        liz = []

        while l <= r and r < len(s):
            while s[r] != '#':
                r += 1
            num = int(s[l:r])
            liz.append(s[r+1 : r+num+1])
            r = r+num+1
            l = r
        return liz
        
