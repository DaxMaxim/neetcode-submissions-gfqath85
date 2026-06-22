class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window, l = set(), 0
        max_len = 0

        for r in range(len(s)):
            # check eligibility
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])

            # capture length
            max_len = max(max_len, r - l + 1)
        return max_len