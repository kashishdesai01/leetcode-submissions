class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        if len(magazine) < len(ransomNote):
            return False

        mag = list(magazine)
        ran = list(ransomNote)

        dic = {}

        for i in range(len(mag)):
            dic[mag[i]] = 1 + dic.get(mag[i], 0)

        for n in ran:
            if n in dic:
                if dic[n] > 0:
                    dic[n] -= 1
                else:
                    return False
            else:
                return False
        return True
            
