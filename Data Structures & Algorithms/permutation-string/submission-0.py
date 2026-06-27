class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False

        # efficient approach
        l, matches = 0, 0
        freqS1, freqS2 = [0]*26, [0]*26

        for st in s1:
            freqS1[ord(st)-ord("a")] += 1
        for i in range(len(s1)):
            freqS2[ord(s2[i])-ord("a")] += 1
        for i in range(26):
            if freqS1[i] == freqS2[i]: matches += 1
        
        for r in range(len(s1), len(s2)):
            # check for matches == 26
            if matches == 26: return True

            # add a new char to freqS2 and update matches
            freqS2[ord(s2[r])-ord("a")] += 1

            if freqS2[ord(s2[r])-ord("a")] == freqS1[ord(s2[r])-ord("a")]:
                matches += 1
            elif freqS2[ord(s2[r])-ord("a")] - 1 == freqS1[ord(s2[r])-ord("a")]:
                matches -= 1

            # remove the left most char from freqS2 and update matches
            freqS2[ord(s2[l])-ord("a")] -= 1

            if freqS2[ord(s2[l])-ord("a")] == freqS1[ord(s2[l])-ord("a")]:
                matches += 1
            elif freqS2[ord(s2[l])-ord("a")] + 1 == freqS1[ord(s2[l])-ord("a")]:
                matches -= 1
            l += 1
        return matches == 26
