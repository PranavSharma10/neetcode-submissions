
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1]*n
        suffix = [1]*n
        p = 1
        q = 1
        for i in range(n):
            prefix[i] = p
            p = p*nums[i]
        for j in range(n-1, -1, -1):
            suffix[j] = q
            q = q*nums[j]

        output = []
        for k in range(n):
            output.append(suffix[k]*prefix[k])
        return output
        
            

