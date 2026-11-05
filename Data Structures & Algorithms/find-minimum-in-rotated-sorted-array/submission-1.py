# first take the array, divide it by half and access that index element,
# for that element check the element on right and left, if element on right is smaller than the current element, then from the right element is your output, return its index
# if the element on the left is smaller take the range from left element to the first element and do the same checks until only 1 element remains, in that case that is your output, its index, and 2 conditions if the value is 
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums [right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

