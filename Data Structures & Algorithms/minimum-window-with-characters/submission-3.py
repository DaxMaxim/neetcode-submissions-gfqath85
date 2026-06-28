class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == "": return ""
        l, res = 0, ""

        window, freqT = defaultdict(int), defaultdict(int)
        
        for i in range(len(t)):
            # window[s[i]] = 1 + window.get(s[i], 0)
            freqT[t[i]] = 1 + freqT.get(t[i], 0)
        
        for r in range(len(s)):
            valid = True
            
            # expand to the right
            window[s[r]] = 1 + window.get(s[r], 0)

            for st in t:
                if freqT[st] > window[st]: valid = False

            # shrink from the left
            while valid:
                # capture the substring
                if r-l+1 < len(res) or res == "": res = s[l : r+1]
                    
                # shrink from left
                window[s[l]] -= 1
                l += 1

                # check validity
                for st in t:
                    if freqT[st] > window[st]: valid = False
        return res

