#i + j = target
#i = target - j
# we start from 0 and subtract from target until we are parsing our list and if our element is in our dict we return true for that counter part

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checkSet = {}
        for i, num in enumerate(nums):
            sub = target - nums[i]
            if sub in checkSet:
                return[checkSet[sub], i]
            checkSet[num] = i
