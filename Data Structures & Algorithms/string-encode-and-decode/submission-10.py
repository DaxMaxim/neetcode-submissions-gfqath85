class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for st in strs:
            res += str(len(st)) + "#" + st
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        l, r = 0, 0

        while r < len(s):
            if s[r] != "#": 
                r += 1
                continue

            num = int(s[l:r])
            res.append(s[r + 1 : r + 1 + num])
            l = r = r + 1 + num
        return res