class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1
        
        missing = len(t)
        start = 0
        bestStart = 0
        bestLen = float('inf')

        for end,ch in enumerate(s):
            if ch in need:
                if need[ch] > 0:
                    missing -= 1
                need[ch] -= 1

            while missing == 0:
                if end - start + 1 < bestLen:
                    bestLen = end - start + 1
                    bestStart = start
                
                left_ch = s[start]
                if left_ch in need:
                    need[left_ch] += 1
                    if need[left_ch] > 0:
                        missing += 1
                start += 1

        if bestLen == float('inf'):
            return ""
        return s[bestStart: bestStart + bestLen]

