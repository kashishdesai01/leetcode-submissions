class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        if len(pattern) != len(words):
            return False

        mapSW, mapWS = {}, {}

        for i in range(len(pattern)):
            c1, w1 = pattern[i], words[i]

            if (c1 in mapSW and mapSW[c1] != w1) or (w1 in mapWS and mapWS[w1] != c1):
                return False

            mapSW[c1] = w1
            mapWS[w1] = c1
        return True