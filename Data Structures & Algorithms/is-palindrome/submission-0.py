# preprocessing - clean string of all aphanumeric chars, spaces and convert to lower
# start 2 pointers, one at the start and one at the end and keep matching until both pointers reach the same letter
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #preprocessing
        cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
        left = 0
        right = len(cleaned) - 1
        while left < right:
            if cleaned[left] != cleaned[right]:
                return False
            left+=1
            right-=1
        return True

