class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Efficient way
        l, most_freq_len, window_len = 0, 0, 0
        freq, res = {}, 0

        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0) 
            most_freq_len = max(most_freq_len, freq[s[r]])

            if (r - l + 1) - most_freq_len > k:
                freq[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res