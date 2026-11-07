class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastSeen = {}
        start = 0
        subMax = 0
        for i, ch in enumerate(s):
            if ch in lastSeen:
                start = max(start, lastSeen[ch] + 1)
            lastSeen[ch] = i
            subMax = max(subMax, i - start + 1)

        return subMax