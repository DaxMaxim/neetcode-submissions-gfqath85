class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for st in strs:
            res += str(len(st)) + "#" + st
        return res

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        start = end = 0
        while end < len(s):
            if s[end] == "#":
                len_of_word = int(s[start:end])
                decoded_list.append(s[end+1 : end + 1 + len_of_word])
                start = end + len_of_word + 1
                end = start
            end += 1
        return decoded_list
            