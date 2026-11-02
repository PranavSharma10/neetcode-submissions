class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = s.lower()
        t = t.lower()
        checkSetS = {}
        checkSetT = {}
        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                checkSetS[s[i]] = checkSetS.get(s[i], 0) + 1
                checkSetT[t[i]] = checkSetT.get(t[i], 0) + 1
        
        return checkSetS == checkSetT