class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        l = 0
        freqS, max_freq = {}, 0

        for r in range(len(s)):
            freqS[s[r]] = 1 + freqS.get(s[r], 0)
            max_freq = max(max_freq, freqS[s[r]])

            if (r - l + 1) - max_freq > k:
                freqS[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
        return max_len