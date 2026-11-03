#a + b + c = 0
#a + b = -c
# [-4, -1, -1, 0, 1, 2]
# to remove dulpicates make a set of values
# (-4, -1, 0, 1, 2)
# 2 pointers, first starts at -4 and second at -1, add them and look for 5 in set
# if yes way to go, else no
# increment -1 to 0 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left<right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left+=1
                elif total > 0:
                    right-=1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left<right and nums[left] == nums[left -1]:
                        left += 1
        return result
            



